def filter_chars(s: str) -> str:
    return ''.join((c for c in s[26:80] if not '<' < c < '>' or c not in s[26:80])) + s[:26] + s[80:]