def remove_repeat_chars(s: str) -> str:
    chars_between_20_93 = set(s[20:93])
    for char in chars_between_20_93:
        if s[20:93].count(char) > 1:
            s = s.replace(char, '', s[20:93].index(char) + 20)
    return s