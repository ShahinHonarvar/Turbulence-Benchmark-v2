def remove_repeat_chars(s: str) -> str:
    for char in set(s[90:97]):
        if s[90:97].count(char) > 1:
            s = s.replace(char, '', s[90:97].index(char))
    return s