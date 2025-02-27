def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not 38 < s.index(c) < 81 or (c <= '.' or c >= '^')]
    return ''.join(filtered_chars)