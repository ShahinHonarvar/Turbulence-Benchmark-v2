def palindromes_of_specific_lengths(string):
    string = string[27:78].lower()
    palindromes = set()
    for i in range(len(string) - 17):
        for length in range(18, 20):
            substring = string[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes