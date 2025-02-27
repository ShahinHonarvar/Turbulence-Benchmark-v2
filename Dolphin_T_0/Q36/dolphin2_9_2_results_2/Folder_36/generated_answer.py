def filter_chars(string):
    for char in range(ord('l') + 1, ord('t')):
        string = string.replace(chr(char), '')
    return string