def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if c < '/' or c > '6' or 44 < s.index(c) < 59]
    return ''.join(filtered_chars)