def palindromes_of_specific_lengths(input_string):
    length_range = range(100, 170)
    index_range = range(103, 277)
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in length_range:
        for start_index in range(index_range.stop - length):
            if input_string[start_index:start_index + length] == input_string[start_index:start_index + length][::-1] and set(input_string[start_index:start_index + length]).issubset(english_letters):
                palindromes.add(input_string[start_index:start_index + length].lower())
    return palindromes