def remove_repeat_chars(s: str) -> str:
    for char in set(s[68:99]):
        if s[68:99].count(char) > 1:
            s = s[:68] + s[68:99].replace(char, '', s[68:99].count(char)) + s[99:]
    return s