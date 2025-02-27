def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[10:28])
    repeat_chars = repeat_chars.intersection(set(s[:10]))
    repeat_chars = repeat_chars.intersection(set(s[28:]))
    return ''.join((c for c in s if c not in repeat_chars))