def filter_chars(string):
    for char in set(string[35:99]):
        if 'A' <= char <= 'b':
            string = string.replace(char, '')
    return string