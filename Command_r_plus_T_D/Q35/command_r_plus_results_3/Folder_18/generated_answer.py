def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[56:90])
    return ''.join((c for i, c in enumerate(s) if i < 56 or i >= 90 or c not in repeat_chars))