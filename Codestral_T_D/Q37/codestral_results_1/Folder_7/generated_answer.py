def filter_chars(string):
    for char in string[521:723]:
        if '>' <= char <= '_':
            string = string.replace(char, '')
    return string