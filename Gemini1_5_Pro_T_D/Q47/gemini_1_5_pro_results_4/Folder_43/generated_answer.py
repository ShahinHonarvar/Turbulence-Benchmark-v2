def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(41, 90):
        for j in range(i, 90):
            substring = s[i:j + 1]
            if len(substring) >= 23 and len(substring) <= 38 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes