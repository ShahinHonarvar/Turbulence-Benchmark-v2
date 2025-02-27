def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[37:43])
    return ''.join((c for i, c in enumerate(s) if i < 37 or i >= 43 or c not in repeat_chars))