def palindromes_of_specific_lengths(s):
    s = s.lower()
    s = s[12:57]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 20, min(i + 22, len(s) + 1)):
            substr = s[i:j]
            if substr.isalpha() and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes