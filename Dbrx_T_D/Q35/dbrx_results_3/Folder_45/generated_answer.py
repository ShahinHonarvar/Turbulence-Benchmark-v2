def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set()
    for i in range(40, 200):
        if s[i] in s[i + 1:200] or s[i] in s[40:i]:
            chars_to_remove.add(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s