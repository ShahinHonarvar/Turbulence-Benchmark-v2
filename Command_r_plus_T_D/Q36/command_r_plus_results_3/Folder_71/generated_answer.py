def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not (82 <= s.index(c) < 89 and '*' < c < '[')]
    return ''.join(filtered_chars)