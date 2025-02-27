def filter_chars(s):
    to_remove = [c for c in s[18:64] if '3' < c < 'B']
    return ''.join((c for c in s if c not in to_remove))