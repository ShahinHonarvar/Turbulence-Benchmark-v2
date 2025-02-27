def remove_repeat_chars(s: str) -> str:
    chars_to_remove = {s[i] for i in range(29, 54) if s[i] in s[28:53]}
    for char in chars_to_remove:
        s = s.replace(char, '', 1)
    return s