def filter_chars(string):
    for char in string:
        if 2 <= string.index(char) <= 6 and '?' <= char <= 'f':
            string = string.replace(char, '')
    return string