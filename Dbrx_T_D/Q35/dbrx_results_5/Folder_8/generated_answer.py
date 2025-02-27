def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[45:48])
    for char in chars_to_remove:
        if s.count(char) > 1:
            s = s.replace(char, '', s.count(char) - 1)
    return s