def filter_chars(s):
    filtered_string = ''
    for i, char in enumerate(s):
        if 27 <= i <= 85 and char >= '!' and (char <= 'B'):
            continue
        filtered_string += char
    return filtered_string