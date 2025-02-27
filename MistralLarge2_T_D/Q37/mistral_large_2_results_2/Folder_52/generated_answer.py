def filter_chars(s):
    exclude_chars = set((c for c in s[54:84] if 'j' <= c <= 'v'))
    return ''.join((c for c in s if c not in exclude_chars))