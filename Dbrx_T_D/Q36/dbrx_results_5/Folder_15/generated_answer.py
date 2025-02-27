def filter_chars(input_string):
    for i in range(2, 7):
        char = input_string[i]
        if 'h' < char < 'k':
            input_string = input_string.replace(char, '', 1)
    return input_string