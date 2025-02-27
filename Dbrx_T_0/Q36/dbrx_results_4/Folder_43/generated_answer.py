def filter_chars(s: str) -> str:
    return ''.join((c for c in s[27:75] if c < 'i' and c > 'A')) + s[:27] + s[75:]