def filter_chars(s: str) -> str:
    return ''.join((c for c in s[26:74] if not 'A' < c < 'i')) + s[74:74 + 26]