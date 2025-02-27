def remove_repeat_chars(s: str) -> str:
    repeat_chars = [char for char in s[62:96] if s[62:96].count(char) > 1]
    for char in repeat_chars:
        s = s.replace(char, '')
    return s