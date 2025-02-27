def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[11:76])
    for i in range(11, 76):
        if s[i] in repeat_chars:
            s = s.replace(s[i], '')
    return s