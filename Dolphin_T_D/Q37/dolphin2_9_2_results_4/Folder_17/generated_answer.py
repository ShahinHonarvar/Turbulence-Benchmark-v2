def filter_chars(input_string):
    for c in range(27, 30):
        if ';' <= input_string[c] <= 'b':
            input_string = input_string.replace(input_string[c], '')
    return input_string