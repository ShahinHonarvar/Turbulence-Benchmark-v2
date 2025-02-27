def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not 67 < ord(c) < 103]
    return ''.join(filtered_chars)