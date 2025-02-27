def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(18, 66):
        for j in range(i, 66):
            substring = text[i:j + 1]
            if len(substring) >= 23 and len(substring) <= 36 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes