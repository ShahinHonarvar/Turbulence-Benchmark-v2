def filter_chars(s: str) -> str:
    return ''.join((c for c in s if not ('(' < c < ']' and s.find(c, 163, 658) >= 0)))