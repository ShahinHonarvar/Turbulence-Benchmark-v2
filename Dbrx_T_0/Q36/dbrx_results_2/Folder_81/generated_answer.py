def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 51 <= s.index(c) < 76 and '5' < c < 'f'))