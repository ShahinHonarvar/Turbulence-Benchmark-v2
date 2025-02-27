def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not (344 < s.index(c) < 874 and 'f' < c < '~')]
    return ''.join(filtered_chars)