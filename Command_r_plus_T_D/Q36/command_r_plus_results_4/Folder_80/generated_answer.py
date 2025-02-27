def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not 54 < s.index(c) < 92 or not 'J' < c < 'X']
    return ''.join(filtered_chars)