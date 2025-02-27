def filter_chars(s: str) -> str:
    return ''.join((c for c in s if s.index(c) < 72 or s.index(c) >= 93 or (ord(c) > ord('<') and ord(c) < ord('J')) or (ord(c) > ord('I') and ord(c) < ord('Z'))))