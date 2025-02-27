def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not 9 < ord(c) < ord('K')]
    return ''.join(filtered_chars)