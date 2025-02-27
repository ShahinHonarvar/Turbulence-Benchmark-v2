def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not (37 <= s.index(c) <= 56 and '6' <= c <= '_')]
    return ''.join(filtered_chars)