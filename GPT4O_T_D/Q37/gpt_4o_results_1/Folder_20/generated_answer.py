def filter_chars(s):
    to_remove = {c for c in s[25:98] if 'm' <= c <= 'w'}
    return ''.join((c for c in s if c not in to_remove))