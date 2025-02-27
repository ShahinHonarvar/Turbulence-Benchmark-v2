def filter_chars(s: str) -> str:
    filter_func = lambda c: c > 'B' and c < 'z'
    return ''.join((c for c in s[318:337] if not filter_func(c))) + s[:318] + s[337:]