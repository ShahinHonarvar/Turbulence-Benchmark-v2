def filter_chars(s: str) -> str:
    return ''.join((c for c in s[343:874] if 'f' < c < '~')) + s[:343] + s[874:]