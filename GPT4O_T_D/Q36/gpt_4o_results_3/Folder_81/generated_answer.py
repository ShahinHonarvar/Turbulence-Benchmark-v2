def filter_chars(s):
    to_remove = {c for c in set(s[52:76]) if '5' < c < 'f'}
    return ''.join((c for c in s if c not in to_remove))