def filter_chars(s: str) -> str:
    chars_to_remove = set(s[35:99]).intersection(set(range(ord('A'), ord('b') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove))