def filter_chars(input_string):
    for char in input_string[41:87]:
        if 'S' <= char <= 's':
            input_string = input_string.replace(char, '')
    return input_string