def filter_chars(string):
    filtered_string = ''
    for char in string:
        if char not in string[7:9] or (char < 'B' or char > 'H'):
            filtered_string += char
    return filtered_string