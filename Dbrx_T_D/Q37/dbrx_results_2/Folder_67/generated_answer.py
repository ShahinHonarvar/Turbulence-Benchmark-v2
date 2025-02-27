def filter_chars(s: str) -> str:
    chars_to_remove = set(range(ord(']'), ord('t') + 1)) & set(range(ord(s[19]), ord(s[22]) + 1))
    return ''.join((c for c in s if c not in chars_to_remove))