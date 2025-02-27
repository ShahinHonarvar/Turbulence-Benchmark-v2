def filter_chars(s: str) -> str:
    chars_to_remove = set((ch for ch in s[2:4] if '5' <= ch <= '_'))
    return ''.join((ch for ch in s if ch not in chars_to_remove))