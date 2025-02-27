def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(16, 78):
        for j in range(i + 42, i + 47):
            substring = text[i:j + 1]
            if len(substring) >= 43 and len(substring) <= 47 and (substring.lower() == substring.lower()[::-1]) and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes