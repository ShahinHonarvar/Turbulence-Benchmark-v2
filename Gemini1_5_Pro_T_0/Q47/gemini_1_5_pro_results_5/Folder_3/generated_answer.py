def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(27, 96):
        for j in range(i + 48, i + 51):
            if j > 95:
                continue
            substring = text[i:j + 1]
            if len(substring) >= 49 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes