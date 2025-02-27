def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 18 <= s.index(c) < 31 and 'H' < c < '|'))