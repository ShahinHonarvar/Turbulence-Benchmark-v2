def filter_chars(s: str) -> str:
    chars_to_remove = set((ch for ch in s[69:87] if '#' < ch < 'L'))
    return ''.join((ch for ch in s if ch not in chars_to_remove))