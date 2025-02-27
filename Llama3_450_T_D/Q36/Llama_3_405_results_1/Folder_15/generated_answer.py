def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 2 < i < 7 and 'h' < c < 'k']
    return ''.join([c for c in s if c not in chars_to_remove])