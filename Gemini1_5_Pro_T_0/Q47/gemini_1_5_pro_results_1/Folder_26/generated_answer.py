def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(24, 85):
        for j in range(i, 85):
            substring = s[i:j + 1]
            if len(substring) >= 21 and len(substring) <= 31 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes