def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not 45 <= ord(c) < 54]
    return ''.join(filtered_chars)