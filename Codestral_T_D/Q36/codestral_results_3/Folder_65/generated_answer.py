def filter_chars(input_string):
    for char in input_string[58:82]:
        if 'F' < char < 'O':
            input_string = input_string.replace(char, '')
    return input_string