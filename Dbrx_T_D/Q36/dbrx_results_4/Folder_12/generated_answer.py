def filter_chars(s: str) -> str:
    return ''.join((c for c in s if not (32 < ord(c) < 84 and 'm' < c < 'w') or c not in s[32:84]))