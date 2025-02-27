def filter_chars(input_string):
    chars_to_remove = set((input_string[i] for i in range(26, 65) if 'V' <= input_string[i] <= 'o'))
    result = ''.join((char for char in input_string if char not in chars_to_remove))
    return result