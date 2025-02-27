def palindromes_of_specific_lengths(string):
    string = string[26:88]
    string = ''.join((char.lower() for char in string if char.isalpha()))
    palindromes = set()
    for length in range(52, 57):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes