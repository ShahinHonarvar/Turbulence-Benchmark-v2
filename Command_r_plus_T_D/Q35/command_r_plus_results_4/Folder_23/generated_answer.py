def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[20:36])
    return ''.join((c for i, c in enumerate(s) if i < 20 or i >= 36 or c not in repeat_chars))