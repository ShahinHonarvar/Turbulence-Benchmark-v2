def palindromes_of_specific_lengths(string):
    string = string[39:95].lower()
    palindromes = set()
    for length in range(14, 53):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes