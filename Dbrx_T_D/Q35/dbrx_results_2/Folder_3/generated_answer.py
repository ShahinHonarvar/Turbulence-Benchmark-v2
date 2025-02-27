def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[56:88])
    for char in s:
        if s.count(char) > 1 and char in chars_to_remove:
            s = s.replace(char, '', s.count(char))
    return s