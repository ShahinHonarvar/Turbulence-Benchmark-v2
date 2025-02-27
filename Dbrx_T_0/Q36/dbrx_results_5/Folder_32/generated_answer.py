def filter_chars(s: str) -> str:
    start, end = (40, 63)
    chars_to_remove = set(filter(lambda c: '7' < c < 'H', s[start:end]))
    return ''.join((c for c in s if c not in chars_to_remove))