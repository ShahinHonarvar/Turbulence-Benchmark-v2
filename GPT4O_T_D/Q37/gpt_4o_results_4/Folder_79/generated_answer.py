def filter_chars(s):
    if len(s) < 10:
        return s
    filter_set = set((c for c in s[10:53] if '@' <= c <= 'T'))
    return ''.join((c for c in s if c not in filter_set))