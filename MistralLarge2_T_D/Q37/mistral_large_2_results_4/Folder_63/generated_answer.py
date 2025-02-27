def filter_chars(s):
    to_remove = {char for i, char in enumerate(s) if 42 <= i <= 92 and '/' <= char <= 'a'}
    return ''.join((char for char in s if char not in to_remove))