def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 18 < i < 64 and '3' < c < 'B']
    return ''.join([c for c in s if c not in chars_to_remove])