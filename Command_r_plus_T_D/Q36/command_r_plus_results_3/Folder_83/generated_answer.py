def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not 72 < ord(c) < 93 or c < '<' or c > 'J']
    return ''.join(filtered_chars)