def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[11:76])
    for char in chars_to_remove:
        s = s.replace(char, '', s[11:76].count(char))
    return s