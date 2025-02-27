def filter_chars(s):
    chars_to_remove = [c for c in s[18:31] if 'H' < c < '|']
    return ''.join((c for c in s if c not in chars_to_remove))