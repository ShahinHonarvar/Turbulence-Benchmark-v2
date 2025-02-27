def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 66 < ord(c) < 89 or (s.index(c) < 669 or s.index(c) > 888) for c in set(s)))