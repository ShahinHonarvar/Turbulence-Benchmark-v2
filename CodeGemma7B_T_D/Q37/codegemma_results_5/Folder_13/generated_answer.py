def filter_chars(string):
    filtered_string = ''
    for char in string:
        if 124 <= ord(char) <= 854 and char >= '9' and (char <= 's'):
            continue
        filtered_string += char
    return filtered_string