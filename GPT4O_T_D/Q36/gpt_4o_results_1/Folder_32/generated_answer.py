def filter_chars(s):
    filtered_chars = set((c for c in s[41:63] if '7' < c < 'H'))
    return ''.join((c for c in s if c not in filtered_chars))