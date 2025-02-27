def palindromes_of_specific_lengths(s):
    s = s.upper()
    s = s[18:66]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 23, min(len(s) + 1, i + 37)):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes