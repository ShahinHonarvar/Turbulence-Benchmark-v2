def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(1, 7):
        for j in range(i + 2, min(i + 5, 9)):
            substring = text[i:j + 1]
            if len(substring) >= 3 and len(substring) <= 4 and (substring.lower() == substring.lower()[::-1]) and all((c.isalpha() for c in substring)):
                palindromes.add(substring.lower())
    return palindromes