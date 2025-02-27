def filter_chars(s: str) -> str:
    return ''.join((c for c in s[283:484] if c <= 'l' or c >= 't')) + s[:283] + s[484:]