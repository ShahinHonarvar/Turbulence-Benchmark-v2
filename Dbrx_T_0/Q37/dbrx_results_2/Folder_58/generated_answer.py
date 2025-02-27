def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 503 <= s.index(c) <= 753 and '9' <= c <= 'w'))