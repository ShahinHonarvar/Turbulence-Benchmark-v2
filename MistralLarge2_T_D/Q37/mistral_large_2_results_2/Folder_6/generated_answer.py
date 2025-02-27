def filter_chars(s):
    to_remove = {char for i, char in enumerate(s) if 13 <= i <= 28 and 'c' <= char <= 'n'}
    return ''.join((char for char in s if char not in to_remove))