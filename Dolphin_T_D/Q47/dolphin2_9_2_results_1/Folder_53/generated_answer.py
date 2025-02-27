def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(1, 300):
        for j in range(i + 2, min(i + 10, len(string) + 1)):
            substring = string[i:j]
            if substring == substring.lower() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes