def remove_repeat_chars(s: str) -> str:
    chars_between_13_and_70 = set(s[12:70])
    for char in chars_between_13_and_70:
        if s[12:70].count(char) > 1:
            s = s.replace(char, '', s[12:70].index(char))
    return s