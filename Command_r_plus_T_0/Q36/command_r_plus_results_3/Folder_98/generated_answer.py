def filter_chars(s: str) -> str:
    chars_to_remove = set((ch for ch in s[4:8] if '1' < ch < 'J'))
    return ''.join((ch for ch in s if ch not in chars_to_remove))