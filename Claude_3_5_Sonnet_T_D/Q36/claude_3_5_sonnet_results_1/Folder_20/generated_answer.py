def filter_chars(s):
    forbidden = set((c for c in s[14:40] if ':' < c < 'C'))
    return ''.join((c for c in s if c not in forbidden))