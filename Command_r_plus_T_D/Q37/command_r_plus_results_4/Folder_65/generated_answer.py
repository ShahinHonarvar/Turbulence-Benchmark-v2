def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not (61 <= s.index(c) <= 70 and '0' <= c <= '@')]
    return ''.join(filtered_chars)