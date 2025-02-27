def filter_chars(string):
    for char in string:
        if ord('S') < ord(char) < ord('['):
            if 78 < string.index(char) < 81:
                string = string.replace(char, '')
    return string