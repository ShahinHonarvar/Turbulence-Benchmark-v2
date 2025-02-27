def remove_repeat_chars(s: str) -> str:
    for char in set(s[355:988]):
        if s[355:988].count(char) > 1:
            s = s.replace(char, '', s[355:988].index(char) + 355)
    return s