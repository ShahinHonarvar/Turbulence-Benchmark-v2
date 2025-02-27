def filter_chars(s: str) -> str:
    return ''.join((c for c in s[:21] + ''.join((c for c in s[21:25] if not '5' < c < '}')) + s[25:] if c not in '5}'))