def palindromes_of_specific_lengths(string):
    palindromes = set()
    string = string.lower()
    for i in range(6):
        for j in range(i + 1, 6):
            substring = string[i:j + 1]
            if substring == substring[::-1] and 3 <= len(substring) <= 5:
                palindromes.add(substring)
    return palindromes