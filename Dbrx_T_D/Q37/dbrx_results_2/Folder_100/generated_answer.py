def filter_chars(s: str) -> str:
    filtered_chars = [c for i, c in enumerate(s) if i < 88 or i > 90 or ord('J') > ord(c) > ord('Q')]
    return ''.join(filtered_chars)