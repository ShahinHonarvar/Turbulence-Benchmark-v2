def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(16, 61):
        for j in range(i, 61):
            substring = text[i - 1:j]
            if len(substring) >= 16 and len(substring) <= 39 and (substring.lower() == substring.lower()[::-1]) and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes