def filter_chars(string):
    for c in string[70:87]:
        if '#' < c < 'L':
            string = string.replace(c, '')
    return string