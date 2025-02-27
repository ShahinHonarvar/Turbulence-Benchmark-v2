def filter_chars(s):
    if len(s) > 3:
        target_chars = set((c for c in s[2:4] if '5' <= c <= '_'))
        return ''.join((c for c in s if c not in target_chars))
    return s