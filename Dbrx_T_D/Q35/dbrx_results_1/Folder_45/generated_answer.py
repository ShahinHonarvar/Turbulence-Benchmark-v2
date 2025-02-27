def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set()
    for i in range(40, 200):
        if s[i] in chars_to_remove:
            s = s[:i] + s[i + 1:]
        elif s[i] in s[:i]:
            chars_to_remove.add(s[i])
    return s