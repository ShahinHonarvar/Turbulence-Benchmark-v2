def filter_chars(s: str) -> str:
    low, high = (ord('t'), ord('x'))
    return ''.join((c for c in s if c < low or c > high or s.index(c) < 42 or (s.index(c) >= 68)))