def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(18, 89):
        for j in range(i + 12, min(i + 15, 89)):
            substring = text[i:j]
            if len(substring) >= 12 and len(substring) <= 14 and (substring.lower() == substring.lower()[::-1]) and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes