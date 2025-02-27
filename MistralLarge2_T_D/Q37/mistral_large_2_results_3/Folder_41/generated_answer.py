def filter_chars(s):
    to_remove = {char for i, char in enumerate(s) if 26 <= i <= 64 and 'V' <= char <= 'o'}
    return ''.join((char for char in s if char not in to_remove))