def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(65, 100):
        for j in range(i, 100):
            substring = text[i:j + 1]
            if 26 <= len(substring) <= 33 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring.lower())
    return palindromes