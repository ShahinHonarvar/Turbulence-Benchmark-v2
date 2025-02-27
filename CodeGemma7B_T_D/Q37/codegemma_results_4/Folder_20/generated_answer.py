def filter_chars(string):
    filtered_string = ''
    for char in string:
        if 25 <= string.index(char) <= 97 and 'm' <= char <= 'w':
            continue
        filtered_string += char
    return filtered_string