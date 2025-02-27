def filter_chars(s: str) -> str:
    chars_to_remove = set(s[83:100])
    return ''.join((c for c in s if c < '*' or c > 'j' or c not in chars_to_remove))