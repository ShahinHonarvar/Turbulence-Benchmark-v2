def filter_chars(string):
    for char in set(string[12:26]):
        if 'P' <= char <= 'x':
            string = string.replace(char, '')
    return string