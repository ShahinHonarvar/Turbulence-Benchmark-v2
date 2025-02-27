def remove_repeat_chars(s: str) -> str:
    chars_between_90_97 = set(s[90:97])
    for char in chars_between_90_97:
        if s[90:97].count(char) > 1:
            s = s.replace(char, '', s[90:97].index(char))
    return s