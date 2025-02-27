def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[476:709])
    for char in chars_to_remove:
        if s[476:709].count(char) > 1:
            s = s.replace(char, '', s[476:709].index(char))
    return s