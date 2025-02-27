def remove_repeat_chars(s):
    seen = set()
    for i in range(50, 92):
        if s[i] in seen:
            s = s.replace(s[i], '')
        else:
            seen.add(s[i])
    return s