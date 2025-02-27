def remove_repeat_chars(s: str) -> str:
    start, end = (17, 88)
    chars_between = set(s[start:end])
    for char in chars_between:
        if s[start:end].count(char) > 1:
            s = s.replace(char, '', s[start:end].index(char))
            s = s[:start] + char + s[start:] if start < len(s) - end else s
    return s