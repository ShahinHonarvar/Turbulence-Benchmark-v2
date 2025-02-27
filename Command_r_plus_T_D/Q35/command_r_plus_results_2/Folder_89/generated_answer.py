def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[55:84])
    return ''.join((c for c in s if c not in repeat_chars))