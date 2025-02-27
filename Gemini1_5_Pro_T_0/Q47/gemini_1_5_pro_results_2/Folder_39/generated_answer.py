def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(31, 92):
        for j in range(i + 49, min(92, i + 53)):
            substring = text[i:j + 1]
            if len(substring) >= 50 and len(substring) <= 53 and (substring.lower() == substring.lower()[::-1]) and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes