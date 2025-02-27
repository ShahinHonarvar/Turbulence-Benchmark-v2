def palindromes_between_indices(string):
    palindromes = set()
    for i in range(5, 8):
        for j in range(i + 3, len(string)):
            substring = string[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring.lower())
    return palindromes