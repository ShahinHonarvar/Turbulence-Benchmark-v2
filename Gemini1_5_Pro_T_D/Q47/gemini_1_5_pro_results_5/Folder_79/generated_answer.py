def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(1, 8):
        for j in range(i + 1, 9):
            substring = text[i:j + 1]
            if 3 <= len(substring) <= 4 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring.lower())
    return palindromes