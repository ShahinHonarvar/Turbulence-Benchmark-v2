def filter_chars(s):
    removal_chars = {c for c in s[32:50] if '/' < c < 'J'}
    return ''.join((c for c in s if c not in removal_chars))