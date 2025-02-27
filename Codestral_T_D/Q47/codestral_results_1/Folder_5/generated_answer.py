def palindromes_of_specific_lengths(s):
    s = s[63:71]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 4, i + 6):
            if j < len(s) and s[i:j + 1].isalpha() and (s[i:j + 1].lower() == s[i:j + 1].lower()[::-1]):
                palindromes.add(s[i:j + 1].lower())
    return palindromes