def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(22, 96):
        for j in range(i + 51, i + 55):
            if j > 95:
                break
            substring = text[i:j + 1]
            if len(substring) >= 52 and len(substring) <= 55 and (substring.lower() == substring.lower()[::-1]) and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes