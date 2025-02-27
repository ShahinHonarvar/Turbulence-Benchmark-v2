def filter_chars(s):
    remove_chars = {c for c in s[2:7] if '-' < c < 'L'}
    return ''.join((c for c in s if c not in remove_chars))