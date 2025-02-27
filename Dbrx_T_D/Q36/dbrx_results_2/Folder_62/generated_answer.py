def filter_chars(s: str) -> str:
    return ''.join((c for c in s if not (c > '*' and c < 'w' and (63 < s.find(c) < 89))))