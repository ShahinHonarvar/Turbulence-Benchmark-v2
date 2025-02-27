def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 90 or i >= 97 or (not 'j' < c < 'w')))