def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 219 < ord(c) < 403 and (not '*' < c < '7')))