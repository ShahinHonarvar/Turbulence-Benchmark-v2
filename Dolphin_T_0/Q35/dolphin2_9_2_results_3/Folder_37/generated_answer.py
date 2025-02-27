def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(2, 7):
        if s[i] in repeat_chars:
            s = s.replace(s[i], '')
        else:
            repeat_chars.add(s[i])
    return s