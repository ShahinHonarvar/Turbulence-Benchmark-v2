def filter_chars(input_string):
    filtered_string = ''
    for char in input_string:
        if 54 < input_string.index(char) < 92:
            if 'J' < char < 'X':
                continue
        filtered_string += char
    return filtered_string