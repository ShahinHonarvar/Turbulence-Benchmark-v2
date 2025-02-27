def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 4 < i < 8 and '1' < c < 'J']
    return ''.join((c for c in s if c not in chars_to_remove))