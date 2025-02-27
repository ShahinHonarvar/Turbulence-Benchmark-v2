def filter_chars(string):
    filtered_string = []
    for char in string:
        if char not in string[27:86] or not (char >= '!' and char <= 'B'):
            filtered_string.append(char)
    return ''.join(filtered_string)