def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not (502 < s.index(c) < 946 and 'W' < c < 'y')]
    return ''.join(filtered_chars)