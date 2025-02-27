def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set()
    for i, char in enumerate(s[2:8]):
        if char in chars_to_remove:
            s = s[:i + 2] + s[i + 3 + 1 if char == s[i + 3] else i + 3:]
        else:
            chars_to_remove.add(char)
    return s