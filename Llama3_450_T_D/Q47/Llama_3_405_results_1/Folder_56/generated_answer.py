def palindromes_of_specific_lengths(s):
    s = s[1:10]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 3, min(i + 8, len(s) + 1)):
            substr = s[i:j]
            if substr.isalpha() and substr.lower() == substr.lower()[::-1]:
                palindromes.add(substr.lower())
    return palindromes