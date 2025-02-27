def filter_chars(string):
    for char in string[61:71]:
        if '0' <= char <= '@':
            string = string.replace(char, '')
    return string