def filter_chars(string):
    for char in range(37, 57):
        for c in string:
            if c >= '6' and c <= '_':
                string = string.replace(c, '')
    return string