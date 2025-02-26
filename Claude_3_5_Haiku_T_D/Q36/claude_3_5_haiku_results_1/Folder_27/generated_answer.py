def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 48 < i < 75 and '6' < c < '_']
    return ''.join((c for c in s if c not in chars_to_remove))