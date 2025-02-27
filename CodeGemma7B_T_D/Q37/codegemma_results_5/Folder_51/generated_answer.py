def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i >= 36 and i <= 40 and (char >= 'H') and (char <= 'e'):
            continue
        filtered_string += char
    return filtered_string