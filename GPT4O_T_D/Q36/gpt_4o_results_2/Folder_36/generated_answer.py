def filter_chars(s):
    if len(s) <= 283:
        return s
    start = 284
    end = min(len(s), 484)
    chars_to_remove = {c for c in s[start:end] if 'l' < c < 't'}
    return ''.join((c for c in s if c not in chars_to_remove))