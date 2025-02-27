def filter_chars(s):
    to_remove = {char for i, char in enumerate(s) if 19 <= i <= 32 and 'f' <= char <= 'o'}
    return ''.join((char for char in s if char not in to_remove))