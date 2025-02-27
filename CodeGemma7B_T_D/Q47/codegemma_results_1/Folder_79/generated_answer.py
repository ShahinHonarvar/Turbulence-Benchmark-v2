def palindromes_of_specific_lengths(some_string):
    palindromes = set()
    for i in range(1, 9):
        for j in range(i, 8):
            substring = some_string[i:j + 1]
            if len(substring) in (3, 4) and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes