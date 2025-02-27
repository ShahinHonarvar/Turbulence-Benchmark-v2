def filter_chars(s: str) -> str:
    chars_to_remove = set((chr(i) for i in range(ord('l') + 1, ord('t'))))
    altered_s = [c for c in s if c not in chars_to_remove or 283 <= s.index(c) < 484]
    return ''.join(altered_s)