def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[103:802])
    unique_chars = []
    for char in s:
        if char in chars_to_remove and char not in unique_chars:
            unique_chars.append(char)
    for char in unique_chars:
        s = s.replace(char, '', s.count(char) - 1)
    return s