def remove_repeat_chars(s: str) -> str:
    chars_between_34_69 = set(s[33:69])
    for char in chars_between_34_69:
        if s[33:69].count(char) > 1:
            s = s.replace(char, '', s[33:69].index(char) + 1)
    return s