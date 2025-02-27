def filter_chars(s: str) -> str:
    return ''.join((c for c in s[26:80] if c < '<' or c > '>')) + s[:26] + s[80:]