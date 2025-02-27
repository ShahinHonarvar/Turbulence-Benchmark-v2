def filter_chars(s: str) -> str:
    return ''.join((c for c in s[475:947] if c <= 'b' or c >= 'd')) + s[:475] + s[947:]