def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(12, 123):
        for j in range(i, 123):
            substring = text[i:j + 1]
            if 12 <= len(substring) <= 220 and substring.lower() == substring.lower()[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes