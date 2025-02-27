def remove_repeat_chars(s: str) -> str:
    char_count = {char: s[s.index(char, 62, 97):].count(char) for char in set(s[62:97])}
    for char, count in char_count.items():
        if count > 1:
            s = s.replace(char, '', count - 1)
    return s