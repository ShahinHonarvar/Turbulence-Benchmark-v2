def filter_chars(string):
    for char in string:
        if 1 <= string.index(char) <= 7 and 'L' <= char <= 'a':
            string = string.replace(char, '')
    return string