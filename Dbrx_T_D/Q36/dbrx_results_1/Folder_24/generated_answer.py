def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 10 <= s.index(c) < 15 and (c > 't' and c < 'v'))) + s[:10] + s[15:]