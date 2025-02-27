def remove_repeat_chars(s: str) -> str:
    for char in set(s[70:98]):
        if s[70:98].count(char) > 1:
            s = s[:70] + s[70:98].replace(char, '') + s[98:]
    return s