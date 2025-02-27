def remove_repeat_chars(s: str) -> str:
    used_chars = set()
    result = []
    for char in s[1:6]:
        if char in used_chars:
            s = s.replace(char, '', 1)
        used_chars.add(char)
    return s