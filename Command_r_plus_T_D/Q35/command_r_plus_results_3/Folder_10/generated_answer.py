def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[36:54])
    return ''.join((c for i, c in enumerate(s) if i < 36 or i >= 54 or c not in repeat_chars))