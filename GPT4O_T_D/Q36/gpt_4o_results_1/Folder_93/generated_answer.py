def filter_chars(s):
    remove_chars = {c for c in s[53:88] if '&' < c < 'c'}
    return ''.join((c for c in s if c not in remove_chars))