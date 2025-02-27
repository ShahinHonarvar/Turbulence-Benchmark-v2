def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[40:200])
    for i in range(40, 200):
        if s[i] in repeat_chars:
            s = s.replace(s[i], '')
    return s