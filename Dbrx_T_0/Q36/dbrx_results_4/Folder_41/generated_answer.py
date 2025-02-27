def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 102 >= ord(c) > 96 or c not in s[81:89]))