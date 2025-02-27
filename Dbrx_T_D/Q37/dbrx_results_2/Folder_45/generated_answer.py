def filter_chars(s: str) -> str:
    chars_to_remove = set(range(ord('.'), ord('b') + 1))
    chars_to_remove &= set(range(ord(s[71]), ord(s[94]) + 1))
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result