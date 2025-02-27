def remove_repeat_chars(s: str) -> str:
    start, end = (45, 48)
    chars_to_remove = set(s[start:end])
    for char in chars_to_remove:
        if s.count(char) > 1:
            s = s.replace(char, '', s.count(char))
    return s