def filter_chars(s):
    to_remove = {c for c in s[587:648] if ',' < c < 'c'}
    return ''.join((c for c in s if c not in to_remove))