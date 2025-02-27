def palindromes_of_specific_lengths(input_string):
    input_string = input_string.lower()
    palindromes = set()
    for length in range(7, 10):
        for i in range(75, 96 - length + 1):
            substring = input_string[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes