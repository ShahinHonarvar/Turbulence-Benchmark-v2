def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not (61 < ord(c) < 88 and '%' < c < 'q')]
    return ''.join(filtered_chars)