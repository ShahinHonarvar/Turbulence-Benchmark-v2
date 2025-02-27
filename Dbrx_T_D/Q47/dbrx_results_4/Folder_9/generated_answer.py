def palindromes_of_specific_lengths(input_string):
    palindromes_set = set()
    for length in range(50, 61):
        for start_index in range(301 - length):
            if input_string[start_index:start_index + length].isalpha() and input_string[start_index:start_index + length].lower() == input_string[start_index:start_index + length][::-1].lower():
                palindromes_set.add(input_string[start_index:start_index + length])
    return palindromes_set