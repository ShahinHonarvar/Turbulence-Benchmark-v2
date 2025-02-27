def remove_repeat_chars(s: str) -> str:
    for char in set(s[69:97]):
        if s[69:97].count(char) > 1:
            s = s[:69] + s[69:97].replace(char, '', s[69:97].count(char) - 1) + s[97:]
    return s