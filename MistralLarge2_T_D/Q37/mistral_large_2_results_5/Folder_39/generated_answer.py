def filter_chars(s):
    filter_set = set(s[52:82])
    filter_set = {c for c in filter_set if 'A' <= c <= 'U'}
    return ''.join((c for c in s if c not in filter_set))