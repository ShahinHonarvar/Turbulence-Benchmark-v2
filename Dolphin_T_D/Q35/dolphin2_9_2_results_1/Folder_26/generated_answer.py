def remove_repeat_chars(s):
    chars = set()
    for i in range(68, 100):
        if s[i] in chars:
            s = s.replace(s[i], '')
        else:
            chars.add(s[i])
    return s