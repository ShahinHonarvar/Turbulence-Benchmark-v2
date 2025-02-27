def filter_chars(s):
    to_filter = set((c for c in s[28:75] if 'A' < c < 'i'))
    return ''.join((c for c in s if c not in to_filter))