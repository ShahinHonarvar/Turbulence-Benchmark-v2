def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 3 < i < 9 and '*' < c < 'E']
    return ''.join((c for c in s if c not in chars_to_remove))