def filter_chars(s: str) -> str:
    return ''.join((c for c in s[14:85] if 'I' < c < 'M')) if 14 < len(s) < 86 else s