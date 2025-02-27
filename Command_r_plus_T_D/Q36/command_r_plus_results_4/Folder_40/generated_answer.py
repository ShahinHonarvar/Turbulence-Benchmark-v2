def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not '-' < c < 'L']
    return ''.join(filtered_chars)