def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not (309 < s.index(c) < 591 and 'S' < c < 'm')]
    return ''.join(filtered_chars)