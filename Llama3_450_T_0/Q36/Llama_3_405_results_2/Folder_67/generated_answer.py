def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 18 < i < 31 and 'H' < c < '|']
    return ''.join((c for c in s if c not in chars_to_remove))