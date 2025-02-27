def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(44, 100):
        for j in range(i, 100):
            substring = text[i:j + 1]
            if 13 <= len(substring) <= 42 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes