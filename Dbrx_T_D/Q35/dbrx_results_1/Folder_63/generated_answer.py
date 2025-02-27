def remove_repeat_chars(s: str) -> str:
    for i in range(81, 87):
        char = s[i]
        if s[:i].count(char) > 0 or s[i:].count(char) > 1:
            s = s[:i] + s[i + 1:]
    return s