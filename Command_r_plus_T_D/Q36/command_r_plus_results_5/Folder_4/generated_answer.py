def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not 6 < ord(c) < ord('g')]
    return ''.join(filtered_chars)