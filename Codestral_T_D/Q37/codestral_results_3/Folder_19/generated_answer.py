def filter_chars(string):
    for char in string[35:90]:
        if 'E' <= char <= 't':
            string = string.replace(char, '')
    return string