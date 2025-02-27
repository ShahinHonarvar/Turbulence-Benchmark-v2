def filter_chars(s):
    exclude = set((c for c in s[13:29] if 'c' <= c <= 'n'))
    return ''.join((c for c in s if c not in exclude))