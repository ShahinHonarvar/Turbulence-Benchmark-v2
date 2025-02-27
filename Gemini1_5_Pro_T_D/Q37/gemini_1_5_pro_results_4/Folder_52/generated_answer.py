def filter_chars(s):
    filtered_chars = set((c for i, c in enumerate(s) if 54 <= i <= 83 and 'j' <= c <= 'v'))
    return ''.join((c for c in s if c not in filtered_chars))