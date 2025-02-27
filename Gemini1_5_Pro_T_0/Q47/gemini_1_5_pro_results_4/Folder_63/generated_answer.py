def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(33, 86):
        for j in range(i + 25, min(86, i + 31)):
            substring = text[i:j + 1]
            if len(substring) >= 26 and len(substring) <= 31 and (substring.lower() == substring.lower()[::-1]) and all((c.isalpha() for c in substring)):
                palindromes.add(substring.lower())
    return palindromes