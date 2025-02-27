def filter_chars(s):
    filtered_chars = set((c for i, c in enumerate(s) if 75 <= i <= 99 and '8' <= c <= 'e'))
    for c in filtered_chars:
        s = s.replace(c, '')
    return s