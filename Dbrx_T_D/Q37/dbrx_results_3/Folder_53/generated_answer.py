def filter_chars(s: str) -> str:
    chars_to_remove = set((ord(c) for c in s[83:100] if ord('*') <= ord(c) <= ord('j')))
    return ''.join((c for c in s if c not in chars_to_remove))