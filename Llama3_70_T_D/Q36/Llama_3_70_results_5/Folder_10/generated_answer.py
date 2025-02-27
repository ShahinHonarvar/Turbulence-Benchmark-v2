def filter_chars(s):
    unique_chars = set([c for c in s[35:60] if '!' < c < 'B'])
    return ''.join([c for c in s if c not in unique_chars])