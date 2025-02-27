def filter_chars(s):
    chars_to_remove = set(s[61:88])
    chars_to_remove = {c for c in chars_to_remove if '%' < c < 'q'}
    return ''.join((c for c in s if c not in chars_to_remove))