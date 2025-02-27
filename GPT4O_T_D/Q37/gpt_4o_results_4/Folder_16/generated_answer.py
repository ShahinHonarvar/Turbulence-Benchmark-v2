def filter_chars(input_string):
    for char in set(input_string[225:382]):
        if 'D' <= char <= 'Y':
            input_string = input_string.replace(char, '')
    return input_string