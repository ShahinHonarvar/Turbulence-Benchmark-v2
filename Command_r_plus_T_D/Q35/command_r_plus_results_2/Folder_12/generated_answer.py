def remove_repeat_chars(s: str) -> str:
    repeated_chars = set(s[16:87])
    repeated_chars = repeated_chars.intersection(s)
    return ''.join((c for c in s if c not in repeated_chars))