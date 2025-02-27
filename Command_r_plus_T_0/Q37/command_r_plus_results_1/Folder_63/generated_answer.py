def filter_chars(s: str) -> str:
    chars_to_remove = set((ch for ch in s[42:93] if '/' <= ch <= 'a'))
    return ''.join((ch for ch in s if ch not in chars_to_remove))