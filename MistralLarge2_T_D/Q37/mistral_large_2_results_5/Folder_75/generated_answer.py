def filter_chars(s: str) -> str:
    chars_to_remove = {ch for i, ch in enumerate(s) if 34 <= i <= 67 and 'W' <= ch <= 'x'}
    return ''.join((ch for ch in s if ch not in chars_to_remove))