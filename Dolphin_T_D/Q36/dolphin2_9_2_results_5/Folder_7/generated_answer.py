def filter_chars(input_string):
    for index in range(502, 946):
        char = input_string[index]
        if char > 'W' and char < 'y':
            input_string = input_string.replace(char, '')
    return input_string