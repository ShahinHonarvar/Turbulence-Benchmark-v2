def palindromes_between_indices(string):
    palindromes = set()
    for i in range(len(string) - 3):
        for j in range(i + 4, len(string) + 1):
            substring = string[i:j].lower()
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes