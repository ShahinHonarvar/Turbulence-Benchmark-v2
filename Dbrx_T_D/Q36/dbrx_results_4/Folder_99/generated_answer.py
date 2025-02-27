def filter_chars(s: str) -> str:
    return s[:476] + ''.join((c for c in s[476:948] if c <= 'b' or c >= 'd')) + s[948:]