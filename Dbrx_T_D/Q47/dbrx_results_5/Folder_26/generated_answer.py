def palindromes_of_specific_lengths(input_string):
    palindromes = set()
    for length in range(21, 32):
        for start_index in range(24, len(input_string) - length + 2):
            substring = input_string[start_index:start_index + length].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes