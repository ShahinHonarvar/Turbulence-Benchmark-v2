def remove_repeat_chars(s: str) -> str:
    char_set = set(s[1:4])
    return ''.join((c for c in s if c not in char_set))