def filter_chars(s):
    to_remove = [c for c in s[502:946] if 'W' < c < 'y']
    return ''.join((c for c in s if c not in to_remove))