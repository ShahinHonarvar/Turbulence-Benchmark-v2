def filter_chars(s):
    chars_to_filter = set((c for i, c in enumerate(s[:44]) if 20 < i <= 43 and '+' <= c <= '8'))
    return ''.join((c for c in s if c not in chars_to_filter))