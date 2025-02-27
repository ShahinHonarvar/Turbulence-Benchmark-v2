def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not 't' < c < 'v' or s.index(c) < 10 or s.index(c) >= 15]
    return ''.join(filtered_chars)