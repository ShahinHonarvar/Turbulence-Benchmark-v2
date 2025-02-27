def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(21):
        for j in range(4, 81):
            substring = string[i:i + j]
            if len(substring) == j and substring == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes