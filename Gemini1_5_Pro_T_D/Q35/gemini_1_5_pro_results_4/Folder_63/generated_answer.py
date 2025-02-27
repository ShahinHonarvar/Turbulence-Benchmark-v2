def remove_repeat_chars(s):
    for i in range(82, 86):
        if s[i] in s[82:i] + s[i + 1:86]:
            s = s.replace(s[i], '')
    return s