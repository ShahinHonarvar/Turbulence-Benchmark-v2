def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(18, 66):
        for j in range(i, 66):
            substring = text[i:j + 1]
            if 23 <= len(substring) <= 36 and substring.lower() == substring.lower()[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes