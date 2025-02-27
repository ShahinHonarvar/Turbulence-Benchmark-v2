def filter_chars(s: str) -> str:
    chars_to_remove = set((ch for ch in s[138:921] if '6' <= ch <= 'A'))
    return ''.join((ch for ch in s if ch not in chars_to_remove))