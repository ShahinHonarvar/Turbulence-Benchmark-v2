def filter_chars(s):
    to_remove = set((c for i, c in enumerate(s) if 227 <= i <= 235 and 'D' <= c <= 'u'))
    return ''.join((c for c in s if c not in to_remove))