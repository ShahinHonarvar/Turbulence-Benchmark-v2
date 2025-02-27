def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[60:200])
    for i in range(60, 200):
        if s[i] in chars_to_remove:
            s = s.replace(s[i], '', i)
    return s