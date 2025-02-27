def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set()
    for i in range(1, 3):
        if s[i] in s[i - 1]:
            chars_to_remove.add(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '', s.count(char))
    return s