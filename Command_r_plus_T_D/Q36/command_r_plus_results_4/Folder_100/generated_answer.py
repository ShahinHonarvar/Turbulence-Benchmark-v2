def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not 43 < s.index(c) < 69 or not 'B' < c < 'r']
    return ''.join(filtered_chars)