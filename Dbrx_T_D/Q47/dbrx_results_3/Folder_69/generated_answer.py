def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(11, 97):
        for j in range(45, 53):
            if i + j - 1 > 96:
                break
            substring = string[i:i + j].lower()
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes