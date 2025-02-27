def remove_repeat_chars(s: str) -> str:
    for char in set(s[22:24]):
        if s[22:24].count(char) > 1:
            s = s[:22] + s[22:24].replace(char, '', 1) + s[24:]
    return s