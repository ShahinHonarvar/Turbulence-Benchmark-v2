def palindromes_of_specific_lengths(input_string):
    input_string = input_string[31:75].lower()
    palindromes = set()
    for length in range(23, 40):
        for start_index in range(len(input_string) - length + 1):
            if input_string[start_index:start_index + length] == input_string[start_index:start_index + length][::-1]:
                palindromes.add(input_string[start_index:start_index + length])
    return palindromes