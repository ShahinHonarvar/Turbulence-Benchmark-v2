def filter_chars(s: str) -> str:
    chars_to_remove = set(s[19:23]) & set(']^_abcdefghijklmnopqrst')
    return ''.join((ch for ch in s if ch not in chars_to_remove))