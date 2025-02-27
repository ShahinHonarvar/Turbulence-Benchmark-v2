def palindromes_of_specific_lengths(input_string):
    palindromes = set()
    input_string = input_string.lower()
    for length in range(52, 56):
        for start_index in range(22, len(input_string) - length + 2):
            substring = input_string[start_index:start_index + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes