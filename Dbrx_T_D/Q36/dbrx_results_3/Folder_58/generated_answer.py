def filter_chars(s: str) -> str:
    start, end = (318, 337)
    chars_to_remove = set(filter(lambda c: 'B' < c < 'z', s[start:end]))
    return ''.join((c for c in s if c not in chars_to_remove))