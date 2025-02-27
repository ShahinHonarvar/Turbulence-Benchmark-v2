def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 1 < s.index(c) < 9 or not '8' < c < 'm'))