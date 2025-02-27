def filter_chars(s: str) -> str:
    chars_to_remove = set(s[515:539])
    return ''.join((c for c in s if c < '+' or c > '}' or c not in chars_to_remove))