def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 24 <= s.index(c) <= 82 and '5' <= c <= '<'))