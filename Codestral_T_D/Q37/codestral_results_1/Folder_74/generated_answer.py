def filter_chars(string):
    for char in string[19:33]:
        if 'f' <= char <= 'o':
            string = string.replace(char, '')
    return string