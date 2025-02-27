def filter_chars(s: str) -> str:
    return ''.join((c for c in s if not ('I' < c < 'a' and 49 < s.index(c) < 58)))