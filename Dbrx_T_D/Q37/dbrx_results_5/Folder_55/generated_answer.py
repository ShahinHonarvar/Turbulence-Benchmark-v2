def filter_chars(input_string):
    for i in range(1, 6):
        char = input_string[i]
        if '$' <= char <= ';':
            input_string = input_string.replace(char, '', 1)
    return input_string