def remove_repeat_chars(s: str) -> str:
    char_count = {char: s[s.index(char, 48, 76):s.index(char, 48, 76) + 1].count(char) for char in set(s[48:76])}
    for char, count in char_count.items():
        if count > 1:
            s = s.replace(char, '', count - 1)
    return s