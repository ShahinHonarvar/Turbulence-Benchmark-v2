def filter_chars(s: str) -> str:
    return ''.join((c for c in s if s.index(c) >= 114 and s.index(c) <= 639 and (ord('!') <= ord(c) <= ord('x'))))