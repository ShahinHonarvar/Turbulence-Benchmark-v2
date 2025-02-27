def filter_chars(s):
    filter_range = {c for c in s[503:754] if '9' <= c <= 'w'}
    return ''.join((c for c in s if c not in filter_range))