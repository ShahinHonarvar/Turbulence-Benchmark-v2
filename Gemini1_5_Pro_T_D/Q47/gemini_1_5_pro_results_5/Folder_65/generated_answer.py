def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(15, 96):
        for j in range(i + 19, min(96, i + 66)):
            substring = text[i:j + 1]
            if len(substring) >= 20 and len(substring) <= 66 and (substring.lower() == substring.lower()[::-1]) and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes