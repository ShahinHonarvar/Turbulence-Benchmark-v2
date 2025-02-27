def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not (65 < ord(c) < 105 and 27 < s.index(c) < 75)]
    return ''.join(filtered_chars)