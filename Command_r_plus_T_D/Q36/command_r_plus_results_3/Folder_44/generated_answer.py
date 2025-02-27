def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not 34 <= ord(c) < 66]
    return ''.join(filtered_chars)