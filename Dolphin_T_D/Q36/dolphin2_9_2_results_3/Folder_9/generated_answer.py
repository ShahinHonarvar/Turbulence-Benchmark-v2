def filter_chars(input_string):
    for i in range(50, 92):
        if input_string[i] > 'A' and input_string[i] < 'Q':
            input_string = input_string.replace(input_string[i], '')
    return input_string