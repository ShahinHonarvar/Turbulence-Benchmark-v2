def filter_chars(s):
    target_range = set(s[41:87])
    remove_chars = {c for c in target_range if 'S' <= c <= 's'}
    return ''.join((c for c in s if c not in remove_chars))