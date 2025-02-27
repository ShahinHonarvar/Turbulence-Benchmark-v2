def filter_chars(s: str) -> str:
    chars_to_remove = set(s[25:98]).intersection(set(range(ord('m')), ord('w') + 1))
    return ''.join((c for c in s if c not in chars_to_remove))