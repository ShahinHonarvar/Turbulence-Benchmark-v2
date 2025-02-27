def remove_repeat_chars(s: str) -> str:
    for char in set(s[7:9]):
        if s[7:9].count(char) > 1:
            s = s[:7] + s[7:].replace(char, '', 1) + s[9:]
    return s