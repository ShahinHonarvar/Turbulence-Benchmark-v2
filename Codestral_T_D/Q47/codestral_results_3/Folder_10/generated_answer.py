def palindromes_of_specific_lengths(string):
    string = string.lower()
    palindromes = set()
    for length in range(16, 40):
        for i in range(16, 61 - length + 1):
            substring = string[i:i + length]
            if substring == substring[::-1]:
                if substring.isalpha():
                    palindromes.add(substring)
    return palindromes