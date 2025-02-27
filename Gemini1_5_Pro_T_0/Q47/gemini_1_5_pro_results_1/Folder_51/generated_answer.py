def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(2, 7):
        for j in range(i + 1, 9):
            substring = string[i:j + 1]
            if 3 <= len(substring) <= 4 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring.lower())
    return palindromes