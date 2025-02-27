def filter_chars(s):
    filtered_chars = set((c for c in s[332:713] if 'M' < c < '_'))
    return ''.join((c for c in s if c not in filtered_chars))