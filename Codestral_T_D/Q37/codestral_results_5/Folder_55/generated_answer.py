def filter_chars(string):
    filtered_string = ''
    for char in string:
        if not (1 <= string.index(char) <= 5 and '$' <= char <= ';'):
            filtered_string += char
    return filtered_string