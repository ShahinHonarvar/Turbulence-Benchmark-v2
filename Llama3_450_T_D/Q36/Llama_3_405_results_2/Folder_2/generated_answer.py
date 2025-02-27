def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 421 < i < 854 and 'D' < c < 'J']
    return ''.join((c for c in s if c not in chars_to_remove))