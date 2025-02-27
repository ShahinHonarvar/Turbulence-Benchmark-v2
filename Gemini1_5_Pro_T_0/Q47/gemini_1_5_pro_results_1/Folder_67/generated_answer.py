def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(65, 100):
        for j in range(i, 100):
            substring = text[i:j + 1].lower()
            if 26 <= len(substring) <= 33 and substring.isalpha() and (substring == substring[::-1]):
                palindromes.add(substring)
    return palindromes