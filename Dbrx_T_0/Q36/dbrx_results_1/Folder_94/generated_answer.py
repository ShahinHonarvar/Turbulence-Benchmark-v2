def filter_chars(s: str) -> str:
    return ''.join((c for c in s[14:85] if c < 'M' and c > 'I')) + s[:14] + s[85:]