def filter_chars(s):
    to_remove = set((c for i, c in enumerate(s) if 513 <= i <= 877 and '?' <= c <= 'n'))
    return ''.join((c for c in s if c not in to_remove))