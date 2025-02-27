def filter_chars(input_string):
    for i in range(38, 55):
        char = input_string[i]
        if ':' <= char <= 'r':
            input_string = input_string.replace(char, '')
    return input_string