def filter_chars(s: str) -> str:
    return ''.join((c for c in s[54:80] if not 'S' < c < 's')) + s[:54] + s[80:]