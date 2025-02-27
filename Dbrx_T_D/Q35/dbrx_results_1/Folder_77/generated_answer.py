def remove_repeat_chars(s: str) -> str:
    chars_between_355_988 = set(s[355:988])
    for char in chars_between_355_988:
        if s[355:988].count(char) > 1:
            s = s.replace(char, '', s[355:988].index(char))
            s = s.replace(char, '', s[355:988].index(char, s[355:988].index(char) + 1))
    return s