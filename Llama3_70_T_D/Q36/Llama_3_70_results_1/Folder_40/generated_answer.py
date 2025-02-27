def filter_chars(s):
    to_remove = set(s[1:7])
    to_remove = {c for c in to_remove if '-' < c < 'L'}
    return ''.join((c for c in s if c not in to_remove))