def filter_chars(s: str) -> str:
    chars_to_remove = set(s[50:78]).intersection(set(range(ord('V'), ord('Z'))))
    return ''.join((c for c in s if c not in chars_to_remove))