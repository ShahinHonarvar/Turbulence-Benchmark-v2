def filter_chars(string):
    for char in string[225:382]:
        if 'D' <= char <= 'Y':
            string = string.replace(char, '')
    return string