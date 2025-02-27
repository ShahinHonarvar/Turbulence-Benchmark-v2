def filter_chars(string):
    new_string = ''
    for i, char in enumerate(string):
        if i >= 41 and i <= 64 and (char >= 'K') and (char <= ']'):
            continue
        new_string += char
    return new_string