def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(125, 283 - 109 + 2):
        for j in range(i + 109 - 1, min(283 + 1, i + 126)):
            substring = text[i:j]
            if len(substring) >= 109 and len(substring) <= 126 and (substring.lower() == substring.lower()[::-1]) and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes