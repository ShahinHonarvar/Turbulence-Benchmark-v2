def filter_chars(s):
    if len(s) < 10:
        return s
    remove_chars = set((c for c in s[7:10] if '6' <= c <= 'w'))
    return ''.join((c for c in s if c not in remove_chars))