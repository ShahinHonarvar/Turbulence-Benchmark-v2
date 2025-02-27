def filter_chars(s):
    to_remove = {char for i, char in enumerate(s) if 24 <= i <= 79 and 'a' <= char <= 'f'}
    return ''.join((char for char in s if char not in to_remove))