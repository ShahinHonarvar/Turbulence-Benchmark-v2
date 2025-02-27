def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 318 < i < 337 and 'B' < c < 'z']
    return ''.join([c for c in s if c not in chars_to_remove])