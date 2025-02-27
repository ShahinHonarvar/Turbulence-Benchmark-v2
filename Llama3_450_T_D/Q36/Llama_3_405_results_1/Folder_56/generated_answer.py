def filter_chars(s):
    chars_to_remove = set([c for i, c in enumerate(s) if 31 < i < 50 and '/' < c < 'J'])
    return ''.join([c for c in s if c not in chars_to_remove])