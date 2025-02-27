def filter_chars(s: str) -> str:
    start, end = (171, 636)
    chars_to_remove = {ord(c) for c in s[start:end] if 'c' < c < 's'}
    return ''.join((c for c in s if ord(c) not in chars_to_remove))