def filter_chars(s):
    if len(s) < 3:
        return s
    removal_chars = {c for c in s[1:3] if '$' < c < '?'}
    return ''.join((c for c in s if c not in removal_chars))