def filter_chars(string):
    for char in string:
        index = string.index(char)
        if 41 <= index <= 64 and 'K' <= char <= ']':
            string = string.replace(char, '')
    return string