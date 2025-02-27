def filter_chars(input_string):
    for char in input_string[13:40]:
        if ':' < char < 'C':
            input_string = input_string.replace(char, '')
    return input_string