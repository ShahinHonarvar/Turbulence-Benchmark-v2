def filter_chars(s: str) -> str:
    return ''.join((c for c in s if not ('#' < c < 'T' and 66 <= s.index(c) < 90)))