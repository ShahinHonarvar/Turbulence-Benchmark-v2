def filter_chars(s):
    to_remove = {char for i, char in enumerate(s) if 10 <= i <= 69 and 'I' <= char <= 'K'}
    return ''.join((char for char in s if char not in to_remove))