def remove_repeat_chars(s):
    for i in range(33, 44):
        if s[i] in s[33:i] + s[i + 1:44]:
            s = s.replace(s[i], '')
    return s