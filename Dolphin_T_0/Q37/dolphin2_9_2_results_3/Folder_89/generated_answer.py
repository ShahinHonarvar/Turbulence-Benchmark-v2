def filter_chars(string):
    for char in range(ord('!'), ord('@') + 1):
        string = string.replace(chr(char), '')
    return string