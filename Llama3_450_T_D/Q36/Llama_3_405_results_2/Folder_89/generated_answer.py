def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 57 < i < 69 and '(' < c < 'W']
    return ''.join([c for c in s if c not in chars_to_remove])