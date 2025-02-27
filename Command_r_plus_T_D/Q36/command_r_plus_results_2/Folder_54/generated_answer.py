def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not 39 < ord(c) < 80]
    return ''.join(filtered_chars)