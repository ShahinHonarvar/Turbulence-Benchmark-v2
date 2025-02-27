def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(26, 88):
        for j in range(i + 51, min(i + 55, 88) + 1):
            substring = text[i:j + 1]
            if len(substring) >= 52 and len(substring) <= 56 and (substring.lower() == substring.lower()[::-1]) and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes