def filter_chars(s: str) -> str:
    return ''.join((c for c in s[153:221] if not 'A' < c < 'f')) + s[:153] + s[221:]