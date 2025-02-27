def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 69 or i > 97 or (ord('V') < ord(c) < ord('j') and c not in s[69:97])))