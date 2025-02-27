def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 56 < s.index(c) < 86 and (not '+' < c < 'w')))