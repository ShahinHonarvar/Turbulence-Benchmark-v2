def filter_chars(string):
    for char in string:
        if 69 <= string.index(char) <= 80 and '@' <= char <= 'p':
            string = string.replace(char, '')
    return string