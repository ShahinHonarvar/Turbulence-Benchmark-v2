def filter_chars(s):
    to_remove = {c for c in s[11:79] if '?' < c < 'm'}
    return ''.join((c for c in s if c not in to_remove))