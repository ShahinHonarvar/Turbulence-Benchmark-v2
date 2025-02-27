def filter_chars(input_string):
    for i in range(502, 946):
        current_char = input_string[i]
        if current_char > 'W' and current_char < 'y':
            input_string = input_string.replace(current_char, '')
    return input_string