def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not 55 < s.index(c) < 80 or not (c > 'S' and c < 's')]
    return ''.join(filtered_chars)