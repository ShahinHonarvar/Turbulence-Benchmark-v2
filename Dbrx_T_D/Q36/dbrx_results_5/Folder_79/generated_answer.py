def filter_chars(s: str) -> str:
    return ''.join((c for c in s[11:46] if ord('!') < ord(c) < ord('A'))) + s[:11] + s[46:]