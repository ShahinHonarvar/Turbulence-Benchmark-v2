def filter_chars(s: str) -> str:
    return ''.join((c for c in s[330:712] if not 'M' < c < '_')) + s[:330] + s[712:]