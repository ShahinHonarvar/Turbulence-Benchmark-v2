def remove_repeat_chars(s: str) -> str:
    for char in set(s[69:97]):
        if s[69:97].count(char) > 1:
            s = s.replace(char, '', s[69:97].index(char))
    return s