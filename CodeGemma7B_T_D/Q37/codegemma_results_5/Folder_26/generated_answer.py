def filter_chars(txt):
    return ''.join([c for c in txt if c not in set('jki') or c < 'i' or c > 'k'])