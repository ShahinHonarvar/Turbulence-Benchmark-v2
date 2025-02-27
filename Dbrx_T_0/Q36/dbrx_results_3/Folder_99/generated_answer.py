def filter_chars(s: str) -> str:
    return ''.join((c for c in s[475:948] if c < 'b' or c > 'd')) + s[:475] + s[948:]