def filter_chars(string):
    for char in range(ord('A'), ord('b') + 1):
        string = string.replace(chr(char), '')
    return string