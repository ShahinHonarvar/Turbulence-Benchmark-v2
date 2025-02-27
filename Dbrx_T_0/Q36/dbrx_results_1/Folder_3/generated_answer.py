def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 42 or i > 78 or (ord('!') < ord(c) < ord('?') and c not in s[42:78])))