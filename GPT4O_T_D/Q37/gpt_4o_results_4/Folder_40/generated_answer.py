def filter_chars(s):
    if len(s) <= 1:
        return s
    special_chars = set((c for c in s[:2] if '*' <= c <= 's'))
    return ''.join((c for c in s if c not in special_chars))