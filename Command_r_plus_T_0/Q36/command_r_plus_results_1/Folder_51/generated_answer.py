def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not (59 <= s.index(c) < 81 and '5' < c < '>')]
    return ''.join(filtered_chars)