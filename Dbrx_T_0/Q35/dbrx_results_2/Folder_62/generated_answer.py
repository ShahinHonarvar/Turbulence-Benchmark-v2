def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[50:92])
    for char in chars_to_remove:
        if s[50:92].count(char) > 1:
            s = s.replace(char, '', s[50:92].index(char))
    return s