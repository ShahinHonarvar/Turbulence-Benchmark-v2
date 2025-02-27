def filter_chars(string):
    for char in set(string[503:754]):
        if '9' <= char <= 'w':
            string = string.replace(char, '')
    return string