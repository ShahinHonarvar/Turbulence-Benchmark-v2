def filter_chars(s):
    target_chars = {c for c in s[18:82] if 'W' <= c <= '['}
    return ''.join((c for c in s if c not in target_chars))