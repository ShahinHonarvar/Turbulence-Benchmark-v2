def filter_chars(s):
    filter_set = set(s[57:97])
    return ''.join((c for c in s if c not in filter_set or c < '<' or c > 'w'))