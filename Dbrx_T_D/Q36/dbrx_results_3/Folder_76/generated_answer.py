def filter_chars(s: str) -> str:
    start, end = (669, 888)
    chars_to_remove = {c for c in s[start:end] if 'B' < c < 'Y'}
    return ''.join((c for c in s if c not in chars_to_remove))