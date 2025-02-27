def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[2:7] if 'h' < c < 'k']
    return ''.join((c for c in s if c not in chars_to_remove))