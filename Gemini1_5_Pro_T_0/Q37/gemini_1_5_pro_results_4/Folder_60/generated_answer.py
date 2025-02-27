def filter_chars(s):
    filtered_chars = set((c for i, c in enumerate(s) if 12 <= i <= 77 and ':' <= c <= 'L'))
    return ''.join((c for c in s if c not in filtered_chars))