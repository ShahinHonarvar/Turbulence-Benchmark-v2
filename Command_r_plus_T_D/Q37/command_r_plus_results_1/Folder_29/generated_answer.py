def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not '&' <= c <= 'v' or not 12 <= s.index(c) <= 88]
    return ''.join(filtered_chars)