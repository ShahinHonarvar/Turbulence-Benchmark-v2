def filter_chars(input_string):
    for char in input_string[13:29]:
        if 'c' <= char <= 'n':
            input_string = input_string.replace(char, '')
    return input_string