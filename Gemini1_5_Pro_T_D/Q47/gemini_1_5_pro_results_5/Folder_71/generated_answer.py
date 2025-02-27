def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(18, 65 + 1):
        for j in range(i, 65 + 1):
            substring = text[i:j + 1]
            if len(substring) < 23 or len(substring) > 36:
                continue
            if substring.lower() == substring[::-1].lower() and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes