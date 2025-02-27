def filter_chars(s: str) -> str:
    chars_to_remove = [ch for ch in s[10:16] if 't' < ch < 'v']
    return ''.join((ch for ch in s if ch not in chars_to_remove))