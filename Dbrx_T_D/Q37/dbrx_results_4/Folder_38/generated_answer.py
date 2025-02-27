def filter_chars(s: str) -> str:
    filtered_chars = [c for i, c in enumerate(s) if 24 <= i <= 79 and (not 'a' <= c <= 'f')]
    return ''.join(filtered_chars)