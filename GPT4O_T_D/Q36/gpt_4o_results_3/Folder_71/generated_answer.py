def filter_chars(s):
    if len(s) <= 82:
        return s
    to_remove = {c for c in s[83:89] if '*' < c < '['}
    return ''.join((c for c in s if c not in to_remove))