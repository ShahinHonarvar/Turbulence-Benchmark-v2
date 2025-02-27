def filter_chars(s):
    if len(s) < 35:
        return s
    chars_to_remove = {c for c in s[35:99] if 'A' <= c <= 'b'}
    return ''.join((c for c in s if c not in chars_to_remove))