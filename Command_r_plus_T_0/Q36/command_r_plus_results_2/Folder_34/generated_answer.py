def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not ('?' < c < 'm' and 10 <= s.index(c) < 79)]
    return ''.join(filtered_chars)