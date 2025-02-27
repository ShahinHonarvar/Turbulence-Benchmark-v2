def filter_chars(s):
    if len(s) <= 4:
        return s
    target_chars = set((c for c in s[4:5] if '7' <= c <= 'o'))
    return ''.join((c for c in s if c not in target_chars))