def filter_chars(s):
    chars_to_filter = set((c for i, c in enumerate(s) if 12 <= i <= 77 and ':' <= c <= 'L'))
    return ''.join((c for c in s if c not in chars_to_filter))