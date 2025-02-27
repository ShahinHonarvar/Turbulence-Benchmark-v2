def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[42:87])
    return ''.join((c for c in s if c not in repeat_chars))