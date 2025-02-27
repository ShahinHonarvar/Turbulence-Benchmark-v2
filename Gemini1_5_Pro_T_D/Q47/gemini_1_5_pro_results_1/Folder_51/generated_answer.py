def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(2, 7):
        for j in range(i + 1, 9):
            substring = text[i:j + 1].lower()
            if 3 <= len(substring) <= 4 and substring.isalpha() and (substring == substring[::-1]):
                palindromes.add(substring)
    return palindromes