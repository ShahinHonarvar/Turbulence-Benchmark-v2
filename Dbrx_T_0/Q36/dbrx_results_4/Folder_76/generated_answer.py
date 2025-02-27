def filter_chars(s: str) -> str:
    return ''.join((c for c in s if s.index(c) < 669 or s.index(c) >= 888 or ((c <= 'B' or c >= 'Y') and s.index(c) >= 669 and (s.index(c) < 888))))