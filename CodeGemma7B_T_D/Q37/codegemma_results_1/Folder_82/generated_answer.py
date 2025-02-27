def filter_chars(string):
    filtered_chars = ''.join([char for char in string if not ('#' <= char <= 'x' and 12 <= string.index(char) <= 25)])
    return filtered_chars