def filter_chars(s):
    to_remove = [c for c in s[66:90] if '#' < c < 'T']
    return ''.join([c for c in s if c not in to_remove])