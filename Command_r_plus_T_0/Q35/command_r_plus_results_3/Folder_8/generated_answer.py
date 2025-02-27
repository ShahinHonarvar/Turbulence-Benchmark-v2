def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[45:48])
    return ''.join((c for i, c in enumerate(s) if i < 45 or i >= 48 or c not in repeat_chars))