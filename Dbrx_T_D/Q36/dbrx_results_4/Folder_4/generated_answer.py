def filter_chars(s: str) -> str:
    start, end = (42, 65)
    chars_to_remove = set(filter(lambda c: '6' < c < 'g', s[start:end]))
    return ''.join(filter(lambda c: c not in chars_to_remove, s))