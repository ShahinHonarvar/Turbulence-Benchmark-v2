def filter_chars(string):
    return ''.join([char for char in string if string.index(char) in range(24, 83) and char not in '<>56789'])