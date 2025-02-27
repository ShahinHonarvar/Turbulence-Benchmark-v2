def filter_chars(s):
    filtered_chars = set((c for c in s[35:99] if 'A' <= c <= 'b'))
    return ''.join((c for c in s if c not in filtered_chars))