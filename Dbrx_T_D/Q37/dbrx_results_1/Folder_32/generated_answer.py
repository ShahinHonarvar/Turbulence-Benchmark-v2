def filter_chars(s: str) -> str:
    return ''.join((c for c in s if not (23 <= s.index(c) <= 89 and 'w' <= c <= '{')))