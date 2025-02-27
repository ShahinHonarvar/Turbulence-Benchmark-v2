def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(26, 85):
        for j in range(i + 30, min(i + 47, 85)):
            substring = text[i:j]
            if len(substring) >= 30 and len(substring) <= 46 and (substring.lower() == substring.lower()[::-1]) and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes