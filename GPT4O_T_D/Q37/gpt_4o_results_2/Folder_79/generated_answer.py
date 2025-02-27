def filter_chars(s):
    filtered_chars = set((c for i, c in enumerate(s) if 10 <= i <= 52 and '@' <= c <= 'T'))
    return ''.join((c for c in s if c not in filtered_chars))