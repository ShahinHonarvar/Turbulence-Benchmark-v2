def filter_chars(input_string):
    for char_val in range(61, 88):
        if '%' < input_string[char_val] < 'q':
            input_string = input_string.replace(input_string[char_val], '')
    return input_string