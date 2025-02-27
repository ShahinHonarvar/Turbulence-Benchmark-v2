def filter_chars(string):
    chars = [char for char in string if 221 <= string.index(char) < 419 and '>' <= char < 'v']
    for char in chars:
        string = string.replace(char, '')
    return string