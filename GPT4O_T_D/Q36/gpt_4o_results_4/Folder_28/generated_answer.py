def filter_chars(s):
    s = list(s)
    to_remove = {c for c in s[32:73] if 'M' < c < 'j'}
    return ''.join((c for c in s if c not in to_remove))