def filter_chars(s):
    to_remove = {c for c in s[69:81] if '@' <= c <= 'p'}
    return ''.join((c for c in s if c not in to_remove))