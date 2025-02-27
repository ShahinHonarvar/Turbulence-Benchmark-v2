def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 116 >= ord(c) > 116 or c not in s[10:16]))