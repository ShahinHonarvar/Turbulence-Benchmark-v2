def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 51 < i < 76 and '5' < c < 'f']
    return ''.join((c for c in s if c not in chars_to_remove))