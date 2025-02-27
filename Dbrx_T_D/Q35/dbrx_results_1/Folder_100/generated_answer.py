def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[43:78])
    for char in chars_to_remove:
        if s[43:78].count(char) > 1:
            s = s.replace(char, '', s[43:78].index(char))
    return s