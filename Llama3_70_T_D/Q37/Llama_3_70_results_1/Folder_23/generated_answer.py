def filter_chars(s):
    to_remove = set((c for i, c in enumerate(s) if 51 <= i <= 77 and 'V' <= c <= 'Y'))
    return ''.join((c for c in s if c not in to_remove))