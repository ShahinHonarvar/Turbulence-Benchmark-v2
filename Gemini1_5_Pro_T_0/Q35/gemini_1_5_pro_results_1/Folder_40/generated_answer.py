def remove_repeat_chars(s):
    for i in range(1, 3):
        if s[i] in s[i + 1:3]:
            s = s.replace(s[i], '')
    return s