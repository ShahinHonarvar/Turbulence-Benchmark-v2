def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[77:84])
    return ''.join((c for i, c in enumerate(s) if i < 77 or i >= 84 or c not in repeat_chars))