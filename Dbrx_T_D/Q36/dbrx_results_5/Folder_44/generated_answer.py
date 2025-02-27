def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 18 or i > 64 or (s[i] > '3' and s[i] < 'B')))