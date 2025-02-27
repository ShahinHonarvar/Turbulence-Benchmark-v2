def remove_repeat_chars(s: str) -> str:
    char_count = {char: s.count(char) for char in set(s[57:84])}
    for char, count in char_count.items():
        if count > 1:
            s = s.replace(char, '', count - 1)
    return s