def filter_chars(s):
    if len(s) <= 80:
        return s
    chk_chars = set((c for c in s[69:81] if '@' <= c <= 'p'))
    return ''.join((c for c in s if c not in chk_chars))