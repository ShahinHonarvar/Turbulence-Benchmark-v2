def filter_chars(s: str) -> str:
    return ''.join((c for c in s if s.index(c) < 283 or s.index(c) >= 484 or (s.index(c) > 282 and s.index(c) < 484 and (c <= 'l') or c >= 't')))