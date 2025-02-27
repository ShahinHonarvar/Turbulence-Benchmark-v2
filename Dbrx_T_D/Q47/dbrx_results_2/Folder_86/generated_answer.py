def palindromes_of_specific_lengths(input_string):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(34, 56):
        for start_index in range(30, len(input_string) - length + 2):
            if set(input_string[start_index:start_index + length]).issubset(english_letters):
                if input_string[start_index:start_index + length].lower() == input_string[start_index:start_index + length][::-1].lower():
                    palindromes.add(input_string[start_index:start_index + length])
    return palindromes