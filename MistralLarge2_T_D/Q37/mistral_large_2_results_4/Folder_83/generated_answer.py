def filter_chars(s):
    exclude = set((c for c in s[29:80] if 'K' <= c <= 'z'))
    return ''.join((c for c in s if c not in exclude))