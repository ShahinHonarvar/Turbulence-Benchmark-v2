def filter_chars(s):
    chars_to_remove = {char for i, char in enumerate(s) if 41 <= i <= 86 and 'S' <= char <= 's'}
    return ''.join((char for char in s if char not in chars_to_remove))