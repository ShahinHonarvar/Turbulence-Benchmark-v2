def filter_chars(s):
    exclude = set((c for c in s[27:86] if 'c' <= c <= 'i'))
    return ''.join((c for c in s if c not in exclude))