def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(18, 99):
        for j in range(i + 31, min(i + 52, 99)):
            substring = text[i:j]
            if len(substring) >= 31 and len(substring) <= 51 and (substring.lower() == substring.lower()[::-1]) and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes