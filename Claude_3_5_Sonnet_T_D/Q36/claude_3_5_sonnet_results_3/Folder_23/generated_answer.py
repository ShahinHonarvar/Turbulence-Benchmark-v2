def filter_chars(s):
    to_remove = [c for c in s[22:25] if '5' < c < '}']
    return ''.join((c for c in s if c not in to_remove))