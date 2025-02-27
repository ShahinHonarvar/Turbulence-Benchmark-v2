def filter_chars(s):
    return ''.join([c for c in s if c not in set(s[71:97]) or c < '_' or c > 'o'])