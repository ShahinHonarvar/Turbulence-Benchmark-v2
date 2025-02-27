def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[2:5])
    return ''.join((c for i, c in enumerate(s) if i < 2 or i >= 5 or c not in repeat_chars))