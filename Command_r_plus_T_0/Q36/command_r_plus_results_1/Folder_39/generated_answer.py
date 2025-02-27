def filter_chars(s: str) -> str:
    chars_to_remove = set((chr(i) for i in range(ord('5') + 1, ord('C'))))
    filtered_string = ''.join((c for c in s if c not in chars_to_remove or 43 <= s.index(c) < 59))
    return filtered_string