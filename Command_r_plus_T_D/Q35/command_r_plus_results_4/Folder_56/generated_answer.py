def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[7:9])
    return ''.join((c for c in s if c not in chars_to_remove))