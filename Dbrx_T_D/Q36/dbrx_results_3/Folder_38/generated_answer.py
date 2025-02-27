def filter_chars(input_string):
    for char in input_string[44:48]:
        if '+' < char < 'l':
            input_string = input_string.replace(char, '', 1)
    return input_string