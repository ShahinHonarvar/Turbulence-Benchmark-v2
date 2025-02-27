def filter_chars(string):
    for char in string:
        if 20 <= string.index(char) <= 62 and 'i' <= char <= 'k':
            string = string.replace(char, '')
    return string