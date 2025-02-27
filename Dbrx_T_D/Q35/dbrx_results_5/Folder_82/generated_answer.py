def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set()
    for i in range(len(s)):
        if i < 30 or i >= 200:
            continue
        char = s[i]
        if char in chars_to_remove:
            s = s[:i] + s[i + 1:]
        else:
            chars_to_remove.add(char)
    return s