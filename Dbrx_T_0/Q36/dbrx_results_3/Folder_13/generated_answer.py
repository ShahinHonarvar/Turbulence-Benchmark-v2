def filter_chars(s: str) -> str:
    return ''.join((c for c in s[323:526] if c <= ')' or c >= 'O')) + s[:323] + s[526:]