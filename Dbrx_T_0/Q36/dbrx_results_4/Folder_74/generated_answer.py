def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 33 < ord(c) < 36 or (not ord('>') < ord(c) < ord('A') and c not in s[33:36])))