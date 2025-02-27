def filter_chars(s):
    chars_to_filter = set((c for i, c in enumerate(s[21:44]) if '+' <= c <= '8'))
    return ''.join((c for c in s if c not in chars_to_filter))