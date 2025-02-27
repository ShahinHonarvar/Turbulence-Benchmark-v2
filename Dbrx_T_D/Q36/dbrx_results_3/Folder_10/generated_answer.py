def filter_chars(s: str) -> str:
    return ''.join((c for c in s[34:60] if not '!' < c < 'B')) + s[:34] + s[60:]