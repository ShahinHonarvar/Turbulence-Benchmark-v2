def filter_chars(string):
    return ''.join([char for char in string if not 32 <= string.index(char) <= 46 or not '0' <= char <= 'k'])