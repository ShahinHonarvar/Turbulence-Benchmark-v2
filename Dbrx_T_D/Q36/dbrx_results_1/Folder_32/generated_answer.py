def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 40 <= s.index(c) < 63 and '7' < c < 'H' or s.index(c) < 40 or s.index(c) >= 63))