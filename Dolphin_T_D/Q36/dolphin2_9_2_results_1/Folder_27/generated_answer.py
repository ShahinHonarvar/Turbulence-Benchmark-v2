def filter_chars(string):
    for i in range(48, 75):
        if string[i] > '6' and string[i] < '_':
            string = string.replace(string[i], '')
    return string