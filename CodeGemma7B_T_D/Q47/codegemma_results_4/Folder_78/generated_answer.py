def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(15, 72 + 1):
        for j in range(i, 72 + 1):
            substring = s[i:j + 1]
            if substring.isalpha() and len(substring) >= 19 and (len(substring) <= 55) and (substring == substring[::-1]):
                palindromes.add(substring.lower())
    return palindromes