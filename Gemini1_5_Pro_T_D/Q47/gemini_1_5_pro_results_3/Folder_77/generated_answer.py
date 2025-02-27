def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(103, 277):
        for j in range(i, 277):
            substring = text[i:j + 1].lower()
            if len(substring) >= 100 and len(substring) <= 169 and substring.isalpha() and (substring == substring[::-1]):
                palindromes.add(text[i:j + 1])
    return palindromes