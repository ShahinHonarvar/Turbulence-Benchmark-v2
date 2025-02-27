def filter_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s) if 21 <= i <= 43 and '+' <= c <= '8'))
    return ''.join((c for c in s if c not in chars_to_remove))