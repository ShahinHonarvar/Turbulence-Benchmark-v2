def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(12, 123):
        for j in range(i, 123):
            substring = text[i:j + 1]
            if len(substring) >= 12 and len(substring) <= 220 and (substring.lower() == substring.lower()[::-1]) and all((c.isalpha() for c in substring)):
                palindromes.add(substring.lower())
    return palindromes