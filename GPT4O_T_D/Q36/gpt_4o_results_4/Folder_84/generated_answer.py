def filter_chars(s):
    filtered_chars = set((c for c in s[172:636] if 'c' < c < 's'))
    return ''.join((c for c in s if c not in filtered_chars))