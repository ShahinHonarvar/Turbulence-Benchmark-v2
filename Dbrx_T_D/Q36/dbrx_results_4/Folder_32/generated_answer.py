def filter_chars(s: str) -> str:
    return ''.join((c for c in s[40:63] if '7' < c < 'H')) + s[:40] + s[63:]