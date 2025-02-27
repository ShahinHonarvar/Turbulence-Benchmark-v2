def filter_chars(s: str) -> str:
    chars_to_remove = set((ch for ch in s[21:44] if '+' <= ch <= '8'))
    return ''.join((ch for ch in s if ch not in chars_to_remove))