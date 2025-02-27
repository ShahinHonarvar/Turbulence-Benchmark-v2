def filter_chars(s):
    removed_chars = [c for c in s[502:946] if 'W' < c < 'y']
    s = ''.join([c for c in s if c not in removed_chars])
    return s