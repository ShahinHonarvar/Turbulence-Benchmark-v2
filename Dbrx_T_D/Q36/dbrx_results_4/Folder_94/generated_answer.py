def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if 73 < ord(c) < 77]
    return ''.join(filtered_chars)