def remove_repeat_chars(s: str):
    seen = set()
    for i in range(13, 76):
        if s[i] not in seen:
            seen.add(s[i])
        else:
            s = s.replace(s[i], '')
    return s