def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not 43 < s.index(c) < 83 or (c <= ':' or c >= 'Q')]
    return ''.join(filtered_chars)