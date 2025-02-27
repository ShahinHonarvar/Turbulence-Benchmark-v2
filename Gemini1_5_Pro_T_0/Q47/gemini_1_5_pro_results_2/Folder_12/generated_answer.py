def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(62, 89):
        for j in range(i, 89):
            substring = s[i:j + 1]
            if 18 <= len(substring) <= 21 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring.lower())
    return palindromes