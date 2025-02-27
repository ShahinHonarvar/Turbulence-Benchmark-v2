def filter_chars(s: str) -> str:
    chars_to_remove = set((ch for ch in s[54:63] if ')' <= ch <= '9'))
    return ''.join((ch for ch in s if ch not in chars_to_remove))