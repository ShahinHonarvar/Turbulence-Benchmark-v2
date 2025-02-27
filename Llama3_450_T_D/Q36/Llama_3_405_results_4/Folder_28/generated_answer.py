def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 31 < i < 73 and 'M' < c < 'j']
    return ''.join((c for c in s if c not in chars_to_remove))