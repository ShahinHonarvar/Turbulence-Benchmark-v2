def filter_chars(s):
    if len(s) <= 94:
        return s
    chars_to_remove = {c for c in s[72:95] if '.' <= c <= 'b'}
    return ''.join((c for c in s if c not in chars_to_remove))