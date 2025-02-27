def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[409:502])
    for char in repeat_chars:
        s = s.replace(char, '')
    return s