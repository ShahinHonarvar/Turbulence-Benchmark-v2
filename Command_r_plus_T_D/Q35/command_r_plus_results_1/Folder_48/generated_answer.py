def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[409:502])
    repeat_chars = repeat_chars.intersection(set(s))
    return ''.join((c for c in s if c not in repeat_chars))