def filter_chars(s: str) -> str:
    return ''.join((c for c in s[:58] + s[82:] if s[58:82].count(c) == 0 or not 'G' <= c <= 'N'))