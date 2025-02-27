def filter_chars(string):
    for char in string:
        if 46 <= string.index(char) <= 85 and '-' <= char <= 'X':
            string = string.replace(char, '')
    return string