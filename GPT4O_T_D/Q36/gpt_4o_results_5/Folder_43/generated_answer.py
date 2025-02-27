def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(ord('A') + 1, ord('i'))))
    return ''.join((c for c in s if c not in chars_to_remove or s.index(c) <= 27 or s.index(c) >= 75))