def remove_repeat_chars(s):
    for i in range(3, 7):
        if s[i] in s[3:i] or s[i] in s[i + 1:7]:
            s = s.replace(s[i], '')
    return s