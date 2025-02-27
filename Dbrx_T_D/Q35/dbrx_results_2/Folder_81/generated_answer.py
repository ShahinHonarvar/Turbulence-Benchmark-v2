def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set()
    for i in range(len(s)):
        if i >= 20 and i < 200 and (s[i] in s[i + 1:]):
            chars_to_remove.add(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '', 1)
    return s