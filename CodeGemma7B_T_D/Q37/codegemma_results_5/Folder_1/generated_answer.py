def filter_chars(input_string):
    filtered_string = ''
    for i, char in enumerate(input_string):
        if i >= 41 and i <= 79 and (char >= 'f') and (char <= '|'):
            continue
        filtered_string += char
    return filtered_string