def remove_repeat_chars(s: str) -> str:
    char_set = set()
    chars_to_remove = set()
    for i in range(2, 7):
        if s[i] in char_set:
            chars_to_remove.add(s[i])
        char_set.add(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '', 1)
    return s