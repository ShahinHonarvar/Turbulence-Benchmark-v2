def filter_chars(s: str) -> str:
    return ''.join((c for c in s if s.index(c) < 18 or s.index(c) >= 31 or (ord('H') < ord(c) < ord('|') and s.replace(c, '', s.index(c) == 18 or s.index(c) == 31))))