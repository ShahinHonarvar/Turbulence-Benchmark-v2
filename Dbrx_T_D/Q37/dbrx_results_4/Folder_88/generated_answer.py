def filter_chars(input_string):
    for i in range(69, 81):
        char = chr(i)
        if '@' <= char <= 'p':
            input_string = input_string.replace(char, '', 1)
    return input_string