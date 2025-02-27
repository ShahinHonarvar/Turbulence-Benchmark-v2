def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[20:43])
    return ''.join((c for i, c in enumerate(s) if i < 20 or i >= 43 or s.count(c) == 1 or (c not in repeat_chars)))