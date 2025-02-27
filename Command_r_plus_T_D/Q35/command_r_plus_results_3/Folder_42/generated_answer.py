def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[18:60])
    repeat_chars = {c for c in repeat_chars if s.count(c) > 1}
    return ''.join((c for c in s if c not in repeat_chars))