def remove_repeat_chars(s: str) -> str:
    chars_between_2_and_7 = set(s[2:8])
    for char in chars_between_2_and_7:
        if s[2:8].count(char) > 1:
            s = s.replace(char, '', s[2:8].index(char))
    return s