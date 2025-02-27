def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[10:76])
    repeat_chars = repeat_chars.intersection(s[:10])
    repeat_chars = repeat_chars.intersection(s[76:])
    return ''.join((c for c in s if c not in repeat_chars))