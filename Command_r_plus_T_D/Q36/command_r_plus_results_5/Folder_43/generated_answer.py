def filter_chars(s: str) -> str:
    chars_to_remove = [chr(i) for i in range(ord('A') + 1, ord('i'))]
    return ''.join([c for c in s if c not in chars_to_remove or 27 <= s.index(c) <= 75])