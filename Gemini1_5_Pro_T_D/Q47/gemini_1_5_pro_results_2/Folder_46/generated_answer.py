def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11, 98):
        for j in range(i + 28, min(98, i + 62)):
            substring = text[i:j]
            if len(substring) >= 29 and len(substring) <= 62 and (substring.lower() == substring.lower()[::-1]) and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes