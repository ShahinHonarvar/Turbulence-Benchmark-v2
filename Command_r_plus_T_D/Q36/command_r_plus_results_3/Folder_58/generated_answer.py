def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not 318 < s.index(c) < 337 or not 'B' < c < 'z']
    return ''.join(filtered_chars)