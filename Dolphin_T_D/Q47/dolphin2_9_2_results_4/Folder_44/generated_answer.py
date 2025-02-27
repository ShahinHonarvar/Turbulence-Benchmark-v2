def palindromes_of_specific_lengths(string):
    string = string[17:98].lower()
    palindromes = set()
    for length in range(31, 52):
        for i in range(0, len(string) - length + 1):
            substring = string[i:i + length]
            if substring == substring[::-1]:
                if all((char.isalpha() for char in substring)):
                    palindromes.add(substring)
    return palindromes