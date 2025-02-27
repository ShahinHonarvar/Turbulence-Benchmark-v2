def filter_chars(s):
    if len(s) < 2:
        return s
    chars_to_remove = {char for char in s[:2] if '*' <= char <= 's'}
    return ''.join((char for char in s if char not in chars_to_remove))