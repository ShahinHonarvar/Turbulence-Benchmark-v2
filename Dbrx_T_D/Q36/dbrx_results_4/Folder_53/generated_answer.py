def filter_chars(s: str) -> str:
    return ''.join((c for c in s if s.index(c) < 90 or s.index(c) >= 97 or (c <= 'j' and c >= 'w')))