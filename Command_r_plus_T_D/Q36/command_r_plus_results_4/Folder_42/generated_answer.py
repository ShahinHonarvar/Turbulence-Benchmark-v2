def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not (42 < s.index(c) < 68 and 't' < c < 'x')]
    return ''.join(filtered_chars)