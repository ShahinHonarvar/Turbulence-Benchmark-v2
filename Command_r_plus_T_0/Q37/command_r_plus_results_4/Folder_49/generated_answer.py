def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[42:98] if '*' <= c <= 'b']
    return ''.join((c for c in s if c not in chars_to_remove))