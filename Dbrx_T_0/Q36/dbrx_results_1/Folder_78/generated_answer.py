def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 37 > ord(c) > 96 or c not in s[29:33]))