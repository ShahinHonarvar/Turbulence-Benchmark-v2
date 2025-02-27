def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(13, 99):
        for j in range(i + 25, i + 30):
            if j > 99:
                continue
            substring = text[i:j + 1]
            if len(substring) >= 26 and len(substring) <= 29 and (substring.lower() == substring.lower()[::-1]) and all((c.isalpha() for c in substring)):
                palindromes.add(substring.lower())
    return palindromes