def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[330:543])
    for char in chars_to_remove:
        if s[330:543].count(char) > 1:
            s = s.replace(char, '', s[330:543].index(char))
    return s