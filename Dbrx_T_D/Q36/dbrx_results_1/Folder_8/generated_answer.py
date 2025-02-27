def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 82 <= s.index(c) < 93 and '!' < c < '*')) or s[s.index(c):s.index(c) + 2]