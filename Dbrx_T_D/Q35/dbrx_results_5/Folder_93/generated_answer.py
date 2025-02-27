def remove_repeat_chars(s: str) -> str:
    chars_between_57_and_85 = set(s[57:85])
    for char in chars_between_57_and_85:
        if s[57:85].count(char) > 1:
            s = s.replace(char, '', s[57:85].index(char))
    return s