def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(11, 83 - 36):
        for j in range(i + 36, i + 61):
            substring = s[i:j + 1]
            if len(substring) >= 37 and len(substring) <= 60 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes