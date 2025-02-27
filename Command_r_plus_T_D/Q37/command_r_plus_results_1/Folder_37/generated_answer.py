def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not (17 <= s.index(c) <= 63 and 'O' <= c <= '^')]
    return ''.join(filtered_chars)