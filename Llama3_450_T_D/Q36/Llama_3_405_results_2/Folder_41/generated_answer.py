def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 81 < i < 89 and 'f' < c < '{']
    return ''.join([c for c in s if c not in chars_to_remove])