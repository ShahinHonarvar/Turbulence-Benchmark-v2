def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not '!' < c < '}' or c in s[39:88]]
    return ''.join(filtered_chars)