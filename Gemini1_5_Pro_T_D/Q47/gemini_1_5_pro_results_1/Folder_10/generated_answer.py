def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(16, 61):
        for j in range(i, 61):
            substring = text[i:j + 1]
            if len(substring) >= 16 and len(substring) <= 39 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes