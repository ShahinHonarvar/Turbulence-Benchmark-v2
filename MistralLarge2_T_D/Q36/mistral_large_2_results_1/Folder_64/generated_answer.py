def filter_chars(s):
    to_remove = {c for c in s[1:7] if '3' < c < '^'}
    return ''.join((c for c in s if c not in to_remove))