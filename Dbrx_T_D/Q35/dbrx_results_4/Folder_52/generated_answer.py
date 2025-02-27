def remove_repeat_chars(s: str) -> str:
    chars_between_38_81 = set(s[38:81])
    for char in chars_between_38_81:
        if s[38:81].count(char) > 1:
            s = s.replace(char, '', s[38:81].index(char))
    return s