def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 82 <= s.index(c) < 93 and (not '!' < c < '*')))