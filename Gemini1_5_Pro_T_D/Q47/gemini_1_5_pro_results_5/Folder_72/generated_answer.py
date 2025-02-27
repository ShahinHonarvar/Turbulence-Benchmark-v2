def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(26, 91):
        for j in range(i + 27, min(i + 59, 91)):
            substring = text[i:j]
            if len(substring) >= 27 and len(substring) <= 58 and (substring.lower() == substring.lower()[::-1]) and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes