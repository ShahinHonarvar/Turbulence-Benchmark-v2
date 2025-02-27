def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 75 < ord(c) < 97 or c not in s[18:95]))