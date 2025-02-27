def remove_repeat_chars(s: str) -> str:
    chars = set()
    for i, char in enumerate(s[1:3]):
        if char in chars:
            s = s[:i + 1] + s[i + 2 + 2:]
        chars.add(char)
    return s