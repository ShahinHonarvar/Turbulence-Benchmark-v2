def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(103, 277):
        for j in range(i + 99, min(277, i + 170)):
            substring = text[i:j + 1]
            if len(substring) >= 100 and len(substring) <= 169 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes