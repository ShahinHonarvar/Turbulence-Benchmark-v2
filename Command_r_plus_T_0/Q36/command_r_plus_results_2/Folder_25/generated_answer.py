def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not 'A' < c < 'h']
    return ''.join(filtered_chars)