def filter_chars(s: str) -> str:
    return ''.join((c for c in s[14:75] if not '9' < c < 'K')) + s[:14] + s[75:]