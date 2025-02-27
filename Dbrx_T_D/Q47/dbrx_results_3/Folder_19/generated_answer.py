def palindromes_of_specific_lengths(input_string):
    palindromes = set()
    for length in range(3, 8):
        for start_index in range(10, len(input_string) - length + 1):
            substring = input_string[start_index:start_index + length].lower()
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    if len(palindromes) == 0:
        return 'No such palindrome with the length specified occurs in the specified index range.'
    return palindromes