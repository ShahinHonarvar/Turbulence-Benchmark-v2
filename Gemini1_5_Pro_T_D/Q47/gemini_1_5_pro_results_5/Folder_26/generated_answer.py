def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(24, 85):
        for j in range(i + 21, min(i + 32, 85)):
            substring = text[i:j]
            if len(substring) >= 21 and len(substring) <= 31 and (substring.lower() == substring.lower()[::-1]) and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes