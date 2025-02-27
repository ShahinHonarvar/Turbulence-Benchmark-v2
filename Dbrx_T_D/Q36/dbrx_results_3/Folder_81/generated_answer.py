def filter_chars(s: str) -> str:
    return ''.join((c for c in s[50:76] if not '5' < c < 'f')) + s[:50] + s[76:]