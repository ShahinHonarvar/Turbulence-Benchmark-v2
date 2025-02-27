def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not (35 <= s.index(c) <= 51 and 'H' <= c <= 's')]
    return ''.join(filtered_chars)