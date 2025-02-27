def filter_chars(s):
    if len(s) < 20:
        return s
    removal_chars = {c for c in s[20:63] if 'i' <= c <= 'k'}
    return ''.join((c for c in s if c not in removal_chars))