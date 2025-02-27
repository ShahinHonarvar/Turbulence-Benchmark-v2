def filter_chars(s):
    to_remove = {c for c in s[18:82] if 'W' <= c <= '['}
    return ''.join((c for c in s if c not in to_remove))