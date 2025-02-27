def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not 47 < ord(c) < 75 or ord(c) <= 38 or ord(c) >= 77]
    return ''.join(filtered_chars)