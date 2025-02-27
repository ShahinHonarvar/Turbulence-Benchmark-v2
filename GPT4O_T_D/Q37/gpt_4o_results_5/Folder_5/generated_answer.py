def filter_chars(s):
    to_remove = set((c for i, c in enumerate(s[24:83]) if '5' <= c <= '<'))
    return ''.join((c for c in s if c not in to_remove))