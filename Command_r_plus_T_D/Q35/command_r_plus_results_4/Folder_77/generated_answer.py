def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[355:988])
    return ''.join((c for i, c in enumerate(s) if i < 355 or i >= 988 or c not in repeat_chars))