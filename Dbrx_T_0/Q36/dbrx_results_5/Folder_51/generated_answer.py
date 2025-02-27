def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 58 <= s.index(c) < 81 or c <= '5' or c >= '>' or (c == '5') or (c == '>')))