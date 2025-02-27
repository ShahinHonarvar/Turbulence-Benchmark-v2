def filter_chars(s):
    filter_set = {c for c in s[10:70] if 'I' <= c <= 'K'}
    return ''.join((c for c in s if c not in filter_set))