def filter_chars(s: str) -> str:
    return ''.join((c for c in s[318:337] if c < 'B' or c > 'z')) + s[:318] + s[337:]