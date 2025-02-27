def filter_chars(s: str) -> str:
    return ''.join((c for c in s if c not in tuple(s[45:91])[1::2] or not 'D' < c < 'H'))