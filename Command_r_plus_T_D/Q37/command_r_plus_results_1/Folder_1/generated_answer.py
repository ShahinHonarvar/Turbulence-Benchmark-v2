def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not 41 <= s.index(c) <= 79 or not 'f' <= c <= '|']
    return ''.join(filtered_chars)