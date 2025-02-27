def filter_chars(s):
    s = list(s)
    to_remove = {c for c in s[46:57] if 'F' < c < 'n'}
    return ''.join((c for c in s if c not in to_remove))