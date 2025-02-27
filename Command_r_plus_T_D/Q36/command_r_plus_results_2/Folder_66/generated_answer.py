def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if ord(c) < 34 or 125 < ord(c)]
    return ''.join(filtered_chars)