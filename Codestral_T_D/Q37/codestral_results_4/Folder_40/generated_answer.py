def filter_chars(string):
    for char in string[0:2]:
        if '*' <= char <= 's':
            string = string.replace(char, '')
    return string