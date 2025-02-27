def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i >= 37 and i <= 56 and (char >= '6') and (char <= '_'):
            filtered_string += string.replace(char, '')
        else:
            filtered_string += char
    return filtered_string