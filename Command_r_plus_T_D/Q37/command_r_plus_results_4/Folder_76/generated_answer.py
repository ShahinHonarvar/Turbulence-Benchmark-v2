def filter_chars(s: str) -> str:
    chars_to_remove = set((ch for ch in s[379:899] if 'M' <= ch <= 'v'))
    return ''.join((ch for ch in s if ch not in chars_to_remove))