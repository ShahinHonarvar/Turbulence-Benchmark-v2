def filter_chars(s: str) -> str:
    return ''.join((c for c in s[153:221] if c < 'A' or c > 'e')) + s[:153] + s[221:]