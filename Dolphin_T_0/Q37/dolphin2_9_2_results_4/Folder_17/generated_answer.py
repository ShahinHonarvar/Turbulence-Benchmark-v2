def filter_chars(string):
    for char in string:
        if 27 <= string.index(char) <= 29 and ord(';') <= ord(char) <= ord('b'):
            string = string.replace(char, '')
    return string