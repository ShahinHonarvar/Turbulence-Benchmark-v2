def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not 41 < s.index(c) < 56 or not 'Z' < c < 'c']
    return ''.join(filtered_chars)