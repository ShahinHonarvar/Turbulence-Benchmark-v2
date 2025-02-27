def filter_chars(s):
    if len(s) <= 43:
        return s
    chars_to_remove = {c for c in s[44:59] if '5' < c < 'C'}
    return ''.join((c for c in s if c not in chars_to_remove))