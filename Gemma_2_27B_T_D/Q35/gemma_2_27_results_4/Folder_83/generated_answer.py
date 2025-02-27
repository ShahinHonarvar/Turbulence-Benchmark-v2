def remove_repeat_chars(s):
    seen = set()
    for i in range(100, 200):
        if i < len(s) and s[i] in seen:
            s = s.replace(s[i], '')
        else:
            seen.add(s[i])
    return s