def filter_chars(s):
    chars_to_filter = set((c for i, c in enumerate(s) if 38 <= i <= 54 and ':' <= c <= 'r'))
    return ''.join((c for c in s if c not in chars_to_filter))