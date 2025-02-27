def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(16, 78):
        for j in range(i + 42, i + 47):
            if j > 77:
                break
            substring = text[i:j + 1]
            if len(substring) >= 43 and len(substring) <= 47 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes