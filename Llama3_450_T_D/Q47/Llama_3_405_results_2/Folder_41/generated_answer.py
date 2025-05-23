def palindromes_of_specific_lengths(s):
    s = s[1:8].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 3, min(i + 5, len(s) + 1)):
            substr = s[i:j]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes