def filter_chars(string):
    for char in string:
        if 36 <= string.index(char) <= 79 and 'a' <= char <= 'i':
            string = string.replace(char, '')
    return string