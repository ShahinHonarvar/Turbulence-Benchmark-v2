def filter_chars(string):
    for c in string[82:89]:
        if '*' < c < '[':
            string = string.replace(c, '')
    return string