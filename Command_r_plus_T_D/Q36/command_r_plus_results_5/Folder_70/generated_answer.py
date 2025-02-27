def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not 170 < ord(c) < 195 or not '!' < c < '}']
    return ''.join(filtered_chars)