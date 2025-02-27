def filter_chars(string):
    for char in string:
        if 12 <= string.index(char) <= 77 and ':' <= char <= 'L':
            string = string.replace(char, '')
    return string