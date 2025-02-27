def filter_chars(s):
    if len(s) <= 71:
        return s
    remove_chars = {c for c in s[71:74] if 'A' < c < 'U'}
    return ''.join((c for c in s if c not in remove_chars))