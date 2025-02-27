def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 72 > ord(c) > 115 or (ord('H') < ord(c) < ord('s') and c not in s[46:69])))