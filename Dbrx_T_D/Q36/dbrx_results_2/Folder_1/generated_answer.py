def filter_chars(s: str) -> str:
    return ''.join((c for c in s if not ('#' < c < 'L' and 69 <= s.index(c) < 87)))