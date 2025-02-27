def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not (13 < i < 40 and ':' < c < 'C' for i, c in enumerate(s))]
    return ''.join(filtered_chars)