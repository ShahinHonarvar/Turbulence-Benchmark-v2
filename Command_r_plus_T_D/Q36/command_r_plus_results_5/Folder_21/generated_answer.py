def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not 219 < s.index(c) < 403 or not '*' < c < '7']
    return ''.join(filtered_chars)