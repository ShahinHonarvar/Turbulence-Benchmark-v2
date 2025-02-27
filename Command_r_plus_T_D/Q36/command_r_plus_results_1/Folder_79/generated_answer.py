def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not ('!' < c < 'A' and 11 < s.index(c) < 46)]
    return ''.join(filtered_chars)