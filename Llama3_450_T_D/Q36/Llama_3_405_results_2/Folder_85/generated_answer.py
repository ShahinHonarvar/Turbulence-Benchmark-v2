def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 55 < i < 80 and 'S' < c < 's']
    return ''.join([c for c in s if c not in chars_to_remove])