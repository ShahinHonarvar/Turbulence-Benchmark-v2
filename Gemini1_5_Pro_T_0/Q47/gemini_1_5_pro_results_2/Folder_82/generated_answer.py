def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(3, 301):
        for j in range(i, 301):
            substring = text[i - 1:j]
            if len(substring) >= 30 and len(substring) <= 300 and (substring.lower() == substring.lower()[::-1]) and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes