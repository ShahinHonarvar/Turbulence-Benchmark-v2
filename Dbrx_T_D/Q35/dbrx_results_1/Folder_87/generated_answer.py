def remove_repeat_chars(s: str) -> str:
    chars_between_20_and_43 = set(s[20:43])
    for char in chars_between_20_and_43:
        if s[20:43].count(char) > 1:
            s = s.replace(char, '', s[20:43].index(char))
    return s