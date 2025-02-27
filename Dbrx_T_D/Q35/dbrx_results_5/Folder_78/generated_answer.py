def remove_repeat_chars(s: str) -> str:
    char_count = {c: s.count(c) for c in set(s)}
    for char, count in list(char_count.items()):
        if 62 < ord(char) < 96 and count > 1:
            s = s.replace(char, '', count - 1)
    return s