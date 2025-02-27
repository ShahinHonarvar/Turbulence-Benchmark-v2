def filter_chars(string):
    for char in string[38:55]:
        if ':' <= char <= 'r':
            string = string.replace(char, '')
    return string