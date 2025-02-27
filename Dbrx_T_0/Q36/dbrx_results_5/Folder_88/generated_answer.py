def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 83 > ord(c) > 78 or c not in s[78:81]))