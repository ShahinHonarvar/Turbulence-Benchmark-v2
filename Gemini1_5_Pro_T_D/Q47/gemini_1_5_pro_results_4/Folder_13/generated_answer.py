def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(13, 96):
        for j in range(i + 56, i + 60):
            if j > 95:
                continue
            substring = text[i:j + 1]
            if len(substring) >= 57 and len(substring) <= 60 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes