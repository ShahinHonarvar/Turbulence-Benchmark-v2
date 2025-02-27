def filter_chars(s: str) -> str:
    return ''.join((c for c in s if not ('*' < c < 'w' and 63 < s.index(c) < 89)))