def palindromes_of_specific_lengths(input_string):
    palindromes = set()
    for length in range(136, 152):
        for index in range(106, len(input_string) - length + 2):
            substring = input_string[index:index + length].lower()
            if substring == substring[::-1] and all((char.isalpha() for char in substring)):
                palindromes.add(substring)
    return palindromes