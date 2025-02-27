def filter_chars(s):
    to_remove = {c for i, c in enumerate(s) if 52 <= i <= 81 and 'A' <= c <= 'U'}
    return ''.join((c for c in s if c not in to_remove))