def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not (42 < s.index(c) < 67 and '6' < c < 'g')]
    return ''.join(filtered_chars)