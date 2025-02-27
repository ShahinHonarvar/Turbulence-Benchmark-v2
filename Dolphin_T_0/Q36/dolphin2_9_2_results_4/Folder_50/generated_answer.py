def filter_chars(input_string):
    for i in range(61, 88):
        if '%' < input_string[i] < 'q':
            input_string = input_string.replace(input_string[i], '')
    return input_string