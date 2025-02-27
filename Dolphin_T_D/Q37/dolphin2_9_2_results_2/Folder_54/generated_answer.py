def filter_chars(string):
    new_string = ''
    for idx, char in enumerate(string):
        if 46 <= idx <= 85 and char >= '-' and (char <= 'X'):
            new_string += ''
        else:
            new_string += char
    return new_string