def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not (669 < s.index(c) < 888 and 'B' < c < 'Y')]
    return ''.join(filtered_chars)