def remove_repeat_chars(s):
    seen = set()
    for i in range(35, 64):
        if s[i] in seen:
            s = s.replace(s[i], '')
        else:
            seen.add(s[i])
    return s