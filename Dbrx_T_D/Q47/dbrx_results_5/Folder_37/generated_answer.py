def palindromes_of_specific_lengths(input_string):
    valid_palindromes = set()
    for length in range(3, 6):
        for index in range(len(input_string) - length + 1):
            if input_string[index:index + length].isalpha() and input_string[index:index + length].lower() == input_string[index:index + length]:
                valid_palindromes.add(input_string[index:index + length])
    return valid_palindromes