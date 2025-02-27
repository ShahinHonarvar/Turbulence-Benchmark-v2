def filter_chars(s):
    if len(s) <= 55:
        return s
    original_chars = s[56:84]
    chars_to_remove = {c for c in original_chars if ';' < c < 'z'}
    return ''.join((c for c in s if c not in chars_to_remove))