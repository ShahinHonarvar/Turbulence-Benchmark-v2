def filter_chars(input_string):
    start_index = 63
    end_index = 84
    char_range_start = 'E'
    char_range_end = '~'
    for index in range(start_index, end_index + 1):
        char_to_remove = chr(index)
        if char_range_start <= char_to_remove <= char_range_end:
            input_string = input_string.replace(char_to_remove, '')
    return input_string