def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(21, 63):
        for j in range(i, 63):
            substring = text[i:j + 1]
            if 22 <= len(substring) <= 33 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes