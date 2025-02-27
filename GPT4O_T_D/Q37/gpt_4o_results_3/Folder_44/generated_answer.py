def filter_chars(s):
    if len(s) < 21:
        return s
    to_remove = set((c for c in s[21:44] if '+' <= c <= '8'))
    return ''.join((c for c in s if c not in to_remove or s.index(c) > 43))