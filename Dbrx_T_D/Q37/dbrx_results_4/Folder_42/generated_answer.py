def filter_chars(s: str) -> str:
    char_to_remove = set(s[73:75]) & set(range(ord('U'), ord('l') + 1))
    return ''.join((c for c in s if c not in char_to_remove))