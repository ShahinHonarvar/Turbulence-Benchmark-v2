def remove_repeat_chars(s: str) -> str:
    chars_to_remove = {char for i, char in enumerate(s) if 62 < i < 96 and s.count(char) > 1}
    for char in chars_to_remove:
        s = s.replace(char, '', s.count(char) - 1)
    return s