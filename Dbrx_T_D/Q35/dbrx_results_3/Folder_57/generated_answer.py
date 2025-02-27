def remove_repeat_chars(s: str) -> str:
    chars_to_remove = {s[i] for i in range(25, 80) if s[i] in s[25:80]}
    for char in chars_to_remove:
        s = s.replace(char, '', s.count(char, 25, 80))
    return s