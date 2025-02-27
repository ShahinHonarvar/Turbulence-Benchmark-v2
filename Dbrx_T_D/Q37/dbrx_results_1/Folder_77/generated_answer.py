def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if 47 <= ord(c) <= 56]
    return ''.join(filtered_chars)