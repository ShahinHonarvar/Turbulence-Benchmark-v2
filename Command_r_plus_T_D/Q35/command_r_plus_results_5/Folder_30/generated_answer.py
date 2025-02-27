def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[22:24])
    return ''.join((c for i, c in enumerate(s) if i < 22 or i >= 24 or c not in chars_to_remove))