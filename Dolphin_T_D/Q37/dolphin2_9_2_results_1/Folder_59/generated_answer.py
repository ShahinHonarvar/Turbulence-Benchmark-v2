def filter_chars(string):
    for char in string[2:4]:
        if '5' <= char <= '_':
            string = string.replace(char, '')
    return string