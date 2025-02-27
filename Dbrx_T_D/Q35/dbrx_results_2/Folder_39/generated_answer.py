def remove_repeat_chars(s: str) -> str:
    start, end = (44, 91)
    chars_to_remove = []
    for i in range(start, end):
        if s[i] in s[start:end]:
            chars_to_remove.append(s[i])
    for char in set(chars_to_remove):
        s = s.replace(char, '')
    return s