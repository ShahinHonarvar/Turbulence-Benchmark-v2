def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[45:49] if '+' < c < 'l']
    return ''.join((c for c in s if c not in chars_to_remove))