def filter_chars(s):
    to_remove = ''.join([c for c in s[69:87] if '#' < c < 'L'])
    return ''.join([c for c in s if c not in to_remove])