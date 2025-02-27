def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not (51 <= s.index(c) <= 77 and 'V' <= c <= 'Y')]
    return ''.join(filtered_chars)