def filter_chars(input_string):
    for char_index in range(18, 82):
        if 'W' <= input_string[char_index] <= '[':
            input_string = input_string.replace(input_string[char_index], '')
    return input_string