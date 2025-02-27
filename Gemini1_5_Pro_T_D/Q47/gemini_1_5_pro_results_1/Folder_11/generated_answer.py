def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(24, 98):
        for j in range(i, 98):
            substring = text[i:j + 1]
            if 10 <= len(substring) <= 36 and substring.lower() == substring.lower()[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring.lower())
    return palindromes