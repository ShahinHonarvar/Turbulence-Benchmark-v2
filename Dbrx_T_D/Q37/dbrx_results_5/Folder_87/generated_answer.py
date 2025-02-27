def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not (18 <= s.index(c) <= 81 and 'W' <= c <= '[')]
    return ''.join(filtered_chars)