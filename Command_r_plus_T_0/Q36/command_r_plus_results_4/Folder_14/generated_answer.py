def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not (42 <= s.index(c) < 57 and 'Z' < c < 'c')]
    return ''.join(filtered_chars)