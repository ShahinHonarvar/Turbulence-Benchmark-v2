def filter_chars(s):
    filtered_string = ''
    for i, char in enumerate(s):
        if 10 <= i <= 69 and 'I' <= char <= 'K':
            filtered_string += ''
        else:
            filtered_string += char
    return filtered_string