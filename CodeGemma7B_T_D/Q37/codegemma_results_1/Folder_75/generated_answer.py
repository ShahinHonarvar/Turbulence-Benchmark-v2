def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i >= 34 and i <= 67 and (char >= 'W') and (char <= 'x'):
            pass
        else:
            filtered_string += char
    return filtered_string