def filter_chars(s: str) -> str:
    chars_to_remove = set((ch for ch in s[56:86] if '+' < ch < 'w'))
    return ''.join((ch for ch in s if ch not in chars_to_remove))