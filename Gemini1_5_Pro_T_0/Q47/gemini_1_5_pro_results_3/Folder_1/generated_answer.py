def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(15, 90):
        for j in range(i + 39, min(i + 73, 90)):
            substring = text[i:j + 1]
            if len(substring) >= 40 and len(substring) <= 72 and (substring.lower() == substring.lower()[::-1]) and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes