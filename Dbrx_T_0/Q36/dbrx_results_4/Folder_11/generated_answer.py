def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 86 <= s.index(c) < 93 and 'E' < c < '~' or c not in s[86:93]))