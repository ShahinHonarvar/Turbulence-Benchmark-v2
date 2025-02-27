def filter_chars(s):
    range_chars = set((c for c in s[83:100] if '*' <= c <= 'j'))
    return ''.join((c for c in s if c not in range_chars))