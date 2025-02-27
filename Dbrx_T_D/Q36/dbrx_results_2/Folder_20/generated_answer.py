def filter_chars(s: str) -> str:
    filter_range = range(ord(':') + 1, ord('C'))
    return ''.join((c for c in s[13:40] if ord(c) not in filter_range)) + s[:13] + s[40:]