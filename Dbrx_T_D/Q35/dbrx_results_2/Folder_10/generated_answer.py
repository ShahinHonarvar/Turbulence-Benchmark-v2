def remove_repeat_chars(s: str) -> str:
    for char in set(s[36:54]):
        if s[36:54].count(char) > 1:
            s = s[:36] + s[36:54].replace(char, '', s[36:54].count(char)) + s[54:]
    return s