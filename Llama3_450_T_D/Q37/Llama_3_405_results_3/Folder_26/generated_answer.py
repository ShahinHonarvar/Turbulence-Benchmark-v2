def filter_chars(s):
    chars_to_filter = set((c for i, c in enumerate(s) if 20 <= i <= 62 and 'i' <= c <= 'k'))
    return ''.join((c for c in s if c not in chars_to_filter))