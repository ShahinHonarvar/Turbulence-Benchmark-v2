def filter_chars(s):
    if len(s) <= 29:
        return s
    to_filter = set(filter(lambda x: 'K' <= x <= 'z', s[29:80]))
    return ''.join((c for c in s if c not in to_filter))