def filter_chars(string):
    for char in range(502, 946):
        if 'W' < string[char] < 'y':
            string = string.replace(string[char], '')
    return string