def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(31):
        for j in range(i + 20, min(i + 31, len(text) + 1)):
            substring = text[i:j]
            if len(substring) >= 20 and len(substring) <= 30 and (substring.lower() == substring.lower()[::-1]) and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes