def remove_repeat_chars(s: str) -> str:
    chars_between_20_and_51 = set(s[20:51])
    for char in chars_between_20_and_51:
        if s[20:51].count(char) > 1:
            s = s.replace(char, '', s[20:51].index(char))
    return s