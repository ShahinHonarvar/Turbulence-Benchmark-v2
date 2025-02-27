def filter_chars(s: str) -> str:
    return ''.join((c for c in s[331:713] if not 'M' < c < '_')) + s[:331] + s[713:]