def filter_chars(s):
    if len(s) > 54:
        chars_to_remove = {c for c in s[38:55] if ':' <= c <= 'r'}
        return ''.join((c for c in s if c not in chars_to_remove))
    return s