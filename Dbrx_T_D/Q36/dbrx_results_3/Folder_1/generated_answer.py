def filter_chars(s: str) -> str:
    return ''.join((c for c in s[69:87] if not '#' < c < 'L')) + s[:69] + s[87:]