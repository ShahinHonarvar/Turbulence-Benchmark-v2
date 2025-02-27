def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 26 < s.index(c) < 80 and (not '<' < c < '>'))) if 26 < len(s) < 80 else s