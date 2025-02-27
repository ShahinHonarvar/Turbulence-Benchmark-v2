def remove_repeat_chars(s: str) -> str:
    window = s[199:202]
    for char in set(window):
        if window.count(char) > 1:
            s = s.replace(char, '', window.count(char))
    return s