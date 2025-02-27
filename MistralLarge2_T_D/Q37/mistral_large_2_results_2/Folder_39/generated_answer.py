def filter_chars(s):
    chars_to_remove = {char for i, char in enumerate(s) if 52 <= i <= 81 and 'A' <= char <= 'U'}
    return ''.join((char for char in s if char not in chars_to_remove))