def filter_chars(s: str) -> str:
    chars_to_remove = set((chr(i) for i in range(ord('<') + 1, ord('C'))))
    return ''.join((c for c in s if c not in chars_to_remove or 19 <= s.index(c) < 69))