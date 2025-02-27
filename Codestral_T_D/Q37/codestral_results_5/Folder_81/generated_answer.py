def filter_chars(string):
    for char in string[19:93]:
        if '8' <= char <= 'm':
            string = string.replace(char, '')
    return string