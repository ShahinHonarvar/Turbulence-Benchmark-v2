def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not (476 < s.index(c) < 948 and 'b' < c < 'd')]
    return ''.join(filtered_chars)