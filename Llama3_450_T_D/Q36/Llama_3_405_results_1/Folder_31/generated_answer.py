def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 14 < i < 75 and '9' < c < 'K']
    return ''.join([c for c in s if c not in chars_to_remove])