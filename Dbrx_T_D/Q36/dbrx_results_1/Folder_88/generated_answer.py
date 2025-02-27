def filter_chars(s: str) -> str:
    return ''.join((c for c in s if s.index(c) < 78 or s.index(c) > 81 or (s.index(c) == 78 or s.index(c) == 81) or (s[78] < c < s[81])))