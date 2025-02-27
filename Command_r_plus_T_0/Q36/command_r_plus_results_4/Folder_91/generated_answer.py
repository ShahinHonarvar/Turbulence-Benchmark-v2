def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[1:4] if '$' < c < '?']
    return ''.join((c for c in s if c not in chars_to_remove))