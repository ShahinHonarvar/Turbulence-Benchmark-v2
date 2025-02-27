def filter_chars(s: str) -> str:
    start, end = (23, 45)
    chars_to_remove = set(filter(lambda c: '3' < c < 'I', s[start:end]))
    return ''.join((c for c in s if c not in chars_to_remove))