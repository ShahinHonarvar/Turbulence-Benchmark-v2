def filter_chars(s: str) -> str:
    chars_to_remove = set((ch for ch in s[35:52] if 'H' <= ch <= 's'))
    return ''.join((ch for ch in s if ch not in chars_to_remove))