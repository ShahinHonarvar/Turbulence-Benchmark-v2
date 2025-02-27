def filter_chars(string):
    for i in range(502, 946):
        if string[i] > 'W' and string[i] < 'y':
            string = string.replace(string[i], '')
    return string