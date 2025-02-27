def remove_repeat_chars(s: str) -> str:
    repeated_chars = set(s[462:995])
    for char in repeated_chars:
        if s[462:995].count(char) > 1:
            s = s.replace(char, '', s[462:995].index(char))
    return s