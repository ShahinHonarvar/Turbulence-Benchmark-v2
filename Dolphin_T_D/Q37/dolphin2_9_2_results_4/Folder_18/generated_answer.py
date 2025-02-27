def filter_chars(string):
    for char in string:
        if 770 <= string.index(char) <= 970 and '-' <= char <= 'D':
            string = string.replace(char, '')
    return string