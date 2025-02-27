def filter_chars(s):
    exclusion_chars = {c for c in s[35:41] if ')' <= c <= 'l'}
    return ''.join((c for c in s if c not in exclusion_chars))