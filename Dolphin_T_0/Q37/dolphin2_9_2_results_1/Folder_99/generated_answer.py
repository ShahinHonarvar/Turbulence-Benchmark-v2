def filter_chars(string):
    chars_to_remove = [c for c in string[373:902] if 'T' <= c <= 'h']
    return ''.join([c for c in string if c not in chars_to_remove])