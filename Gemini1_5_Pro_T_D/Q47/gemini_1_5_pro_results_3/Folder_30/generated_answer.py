def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(14, 91):
        for j in range(i + 55, min(i + 72, 91)):
            substring = text[i:j]
            if len(substring) >= 55 and len(substring) <= 71 and (substring.lower() == substring.lower()[::-1]) and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes