def filter_chars(s):
    if len(s) <= 25:
        return s
    chars_to_remove = {c for c in s[25:37] if 'A' < c < 'h'}
    return ''.join((c for c in s if c not in chars_to_remove))