def filter_chars(s: str) -> str:
    chars_to_remove = set((ch for ch in s[1:7] if '3' < ch < '^'))
    return ''.join((ch for ch in s if ch not in chars_to_remove))