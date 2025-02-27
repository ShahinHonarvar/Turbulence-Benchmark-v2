def filter_chars(s):
    filtered_chars = set((c for c in s[51:78] if 'V' <= c <= 'Y'))
    return ''.join((c for c in s if c not in filtered_chars))