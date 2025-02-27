def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 3 < i < 5 and 'Y' < c < 's']
    return ''.join((c for c in s if c not in chars_to_remove))