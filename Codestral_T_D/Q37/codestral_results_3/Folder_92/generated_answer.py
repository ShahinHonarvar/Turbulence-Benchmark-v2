def filter_chars(string):
    filtered_string = ''
    for char in string:
        if not '7' <= char <= 'o' or string.index(char) != 4:
            filtered_string += char
    return filtered_string