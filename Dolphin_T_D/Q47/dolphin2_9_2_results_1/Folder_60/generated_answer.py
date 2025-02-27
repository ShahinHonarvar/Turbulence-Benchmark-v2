def palindromes_of_specific_lengths(string):
    string = string[23:83]
    palindromes = set()
    for i in range(23, 83):
        for length in range(32, 35):
            substring = string[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes