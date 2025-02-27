def remove_repeat_chars(s: str) -> str:
    chars = s[450:905]
    for char in set(chars):
        if chars.count(char) > 1:
            s = s.replace(char, '', chars.count(char))
    return s