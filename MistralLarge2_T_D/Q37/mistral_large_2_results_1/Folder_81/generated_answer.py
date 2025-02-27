def filter_chars(s):
    to_remove = {char for i, char in enumerate(s) if 19 <= i <= 92 and '8' <= char <= 'm'}
    return ''.join((char for char in s if char not in to_remove))