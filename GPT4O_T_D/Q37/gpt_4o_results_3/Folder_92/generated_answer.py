def filter_chars(s):
    if len(s) <= 4:
        return s
    chars_to_remove = {c for c in s[4:5] if '7' <= c <= 'o'}
    return ''.join((c for c in s if c not in chars_to_remove))