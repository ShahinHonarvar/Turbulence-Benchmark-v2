def palindromes_of_specific_lengths(string):
    string = string[25:88]
    string = string.lower()
    palindromes = set()
    for length in range(52, 57):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if all((char.isalpha() for char in substring)):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes