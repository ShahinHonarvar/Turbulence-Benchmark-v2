def filter_chars(s):
    if len(s) < 4:
        return s
    to_remove = {c for i, c in enumerate(s[2:4]) if '5' <= c <= '_'}
    return ''.join((c for c in s if c not in to_remove))