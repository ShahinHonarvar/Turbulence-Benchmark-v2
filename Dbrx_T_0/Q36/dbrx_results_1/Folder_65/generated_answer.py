def filter_chars(s: str) -> str:
    return ''.join((c for c in s if c < 'F' or c > 'O' or s.index(c) < 58 or (s.index(c) >= 82)))