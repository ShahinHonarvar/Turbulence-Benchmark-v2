def filter_chars(s: str) -> str:
    chars_to_remove = set((chr(i) for i in range(ord('3') + 1, ord('B'))))
    return ''.join((c for c in s if c not in chars_to_remove or 18 <= s.index(c) < 64))