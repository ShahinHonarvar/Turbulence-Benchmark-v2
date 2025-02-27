def remove_repeat_chars(s: str) -> str:
    chars_to_remove = [c for c in set(s[16:87]) if s.count(c) > 1]
    return ''.join([c for c in s if c not in chars_to_remove])