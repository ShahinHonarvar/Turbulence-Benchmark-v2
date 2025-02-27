def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not (672 < s.index(c) < 709 and 'X' < c < '}')]
    return ''.join(filtered_chars)