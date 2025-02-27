def filter_chars(s: str) -> str:
    valid_chars = [c for c in s if 56 <= s.index(c) < 86 and c > '+' and (c < 'w')]
    return ''.join(valid_chars)