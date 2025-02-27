def remove_repeat_chars(s: str) -> str:
    for char in set(s[80:200]):
        if s[80:200].count(char) > 1:
            s = s[:80] + s[80:].replace(char, '', 1).replace(char, '', s[80:].count(char))
    return s