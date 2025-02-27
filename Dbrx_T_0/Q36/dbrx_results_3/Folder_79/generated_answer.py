def filter_chars(s: str) -> str:
    return ''.join((c for c in s[11:46] if not '!' < c < 'A')) + s[:11] + s[46:]