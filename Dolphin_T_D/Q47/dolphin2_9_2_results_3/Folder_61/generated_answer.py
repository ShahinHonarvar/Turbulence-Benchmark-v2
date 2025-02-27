def palindromes_of_specific_lengths(string):
    string = string[:31]
    palindromes = set()
    for length in range(20, 31):
        for i in range(0, 31 - length + 1):
            substring = string[i:i + length]
            if substring == substring.lower() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes