def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(1, 9):
        for j in range(i + 2, min(len(text), 10)):
            substring = text[i:j].lower()
            if 3 <= len(substring) <= 7 and substring.isalpha() and (substring == substring[::-1]):
                palindromes.add(substring)
    return palindromes