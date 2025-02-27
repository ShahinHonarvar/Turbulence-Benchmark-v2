def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[6:9])
    return ''.join((c for i, c in enumerate(s) if i < 6 or i >= 9 or c not in repeat_chars))