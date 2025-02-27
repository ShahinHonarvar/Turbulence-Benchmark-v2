def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(44, 100):
        for j in range(i, 100):
            substring = text[i:j + 1].lower()
            if 13 <= len(substring) <= 42 and substring.isalpha() and (substring == substring[::-1]):
                palindromes.add(text[i:j + 1])
    return palindromes