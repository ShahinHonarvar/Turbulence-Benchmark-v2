def filter_chars(s):
    chars = set((c for c in s[75:100] if '8' <= c <= 'e'))
    return ''.join((c for c in s if c not in chars))