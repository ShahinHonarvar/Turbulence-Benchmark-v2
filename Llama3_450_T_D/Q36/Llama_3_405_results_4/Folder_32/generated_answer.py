def filter_chars(s):
    to_remove = [c for i, c in enumerate(s) if 40 < i < 63 and '7' < c < 'H']
    return ''.join((c for c in s if c not in to_remove))