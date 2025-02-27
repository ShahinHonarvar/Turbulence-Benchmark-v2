def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not (40 <= s.index(c) < 63 and '7' < c < 'H')]
    return ''.join(filtered_chars)