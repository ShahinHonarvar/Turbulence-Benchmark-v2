def filter_chars(s: str) -> str:
    return ''.join((c for c in s[421:854] if c <= 'D' or c >= 'J')) + s[:421] + s[854:]