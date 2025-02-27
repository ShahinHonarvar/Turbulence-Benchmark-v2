def palindromes_of_specific_lengths(string):
    string = string[:101]
    palindromes = set()
    for length in range(3, 16):
        for start_index in range(0, 101 - length + 1):
            substring = string[start_index:start_index + length]
            substring = ''.join(filter(str.isalpha, substring)).lower()
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes