def filter_chars(input_string):
    start_index = 43
    end_index = 83
    char_range = range(ord(':') + 1, ord('Q'))
    for i in char_range:
        input_string = input_string.replace(chr(i), '', start_index, end_index)
    return input_string