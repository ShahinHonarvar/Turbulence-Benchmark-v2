def filter_chars(s: str) -> str:
    chars_to_remove = set(s[4:5]) & set(range(ord('7'), ord('o') + 1))
    return ''.join((c for c in s if c not in chars_to_remove))