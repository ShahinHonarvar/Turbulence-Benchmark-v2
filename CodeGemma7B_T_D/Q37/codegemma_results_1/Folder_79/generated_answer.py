def filter_chars(s):
    return ''.join([c for c in s if c not in set(s[10:53]) or c < '@' or c > 'T'])