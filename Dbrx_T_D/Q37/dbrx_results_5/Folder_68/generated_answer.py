def filter_chars(string):
    return ''.join((char for char in string if 7 <= string.index(char) <= 9 and '6' <= char <= 'w'))